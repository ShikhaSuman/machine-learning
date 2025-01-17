{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# MALICIOUS URL DETECTION"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import random\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                      url label\n",
      "0  diaryofagameaddict.com   bad\n",
      "1        espdesign.com.au   bad\n",
      "2      iamagameaddict.com   bad\n",
      "3           kalantzis.net   bad\n",
      "4   slightlyoffcenter.net   bad\n"
     ]
    }
   ],
   "source": [
    "data = pd.read_csv(\"data.csv\")\n",
    "\n",
    "# Labels\n",
    "y = data[\"label\"]\n",
    "\n",
    "# Features\n",
    "url_list = data[\"url\"]\n",
    "\n",
    "print(data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feature Scaling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  (0, 159634)\t0.09828814616410146\n",
      "  (0, 175869)\t0.9951579976685231\n",
      "  (1, 118202)\t0.40633278478887824\n",
      "  (1, 191405)\t0.9093009006387917\n",
      "  (1, 159634)\t0.08980835207928868\n",
      "  (2, 231248)\t0.9951579976685231\n",
      "  (2, 159634)\t0.09828814616410146\n",
      "  (3, 298267)\t0.303969945214345\n",
      "  (3, 250467)\t0.9526816217427457\n",
      "  (4, 362379)\t0.9526816217427457\n",
      "  (4, 298267)\t0.303969945214345\n",
      "  (5, 386231)\t0.9951579976685231\n",
      "  (5, 159634)\t0.09828814616410146\n",
      "  (6, 392378)\t0.9951579976685231\n",
      "  (6, 159634)\t0.09828814616410146\n",
      "  (7, 225206)\t0.6117149676838319\n",
      "  (7, 238730)\t0.7910782504351694\n",
      "  (8, 193147)\t0.2654997608444888\n",
      "  (8, 315778)\t0.4095532903526943\n",
      "  (8, 322974)\t0.1480898838127254\n",
      "  (8, 237269)\t0.3893592531789013\n",
      "  (8, 386995)\t0.46825210951603796\n",
      "  (8, 397947)\t0.2322520197507969\n",
      "  (8, 164354)\t0.5612875367265502\n",
      "  (9, 257109)\t0.8082847249792281\n",
      "  :\t:\n",
      "  (420457, 110200)\t0.4908284887636513\n",
      "  (420457, 204992)\t0.10314507433042858\n",
      "  (420457, 236271)\t0.07580882757054604\n",
      "  (420458, 167134)\t0.5697450058486412\n",
      "  (420458, 287035)\t0.5399533599637437\n",
      "  (420458, 225580)\t0.4563176362525794\n",
      "  (420458, 178383)\t0.27587466528438825\n",
      "  (420458, 278410)\t0.31038988856027483\n",
      "  (420458, 159634)\t0.05627164786125835\n",
      "  (420459, 29710)\t0.5196086129311506\n",
      "  (420459, 41797)\t0.5386287340705759\n",
      "  (420459, 43502)\t0.5329254989123795\n",
      "  (420459, 44039)\t0.3948118397544405\n",
      "  (420460, 152249)\t0.8254226785385622\n",
      "  (420460, 113118)\t0.5133785707220647\n",
      "  (420460, 312127)\t0.23477615909115532\n",
      "  (420461, 231829)\t0.8527970069942947\n",
      "  (420461, 113118)\t0.47493518304619725\n",
      "  (420461, 312127)\t0.21719538845575861\n",
      "  (420462, 397614)\t0.8527970069942947\n",
      "  (420462, 113118)\t0.47493518304619725\n",
      "  (420462, 312127)\t0.21719538845575861\n",
      "  (420463, 354655)\t0.5392317143321196\n",
      "  (420463, 113118)\t0.6839667195909312\n",
      "  (420463, 236271)\t0.49134375415839354\n"
     ]
    }
   ],
   "source": [
    "# Using Tokenizer\n",
    "vectorizer = TfidfVectorizer()\n",
    "\n",
    "# Store vectors into X variable as  XFeatures\n",
    "X = vectorizer.fit_transform(url_list)\n",
    "print(X)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Splitting the dataset into the Training set and Test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  (0, 190114)\t0.6384948581330733\n",
      "  (0, 297396)\t0.5414439681921646\n",
      "  (0, 258290)\t0.48315809243448327\n",
      "  (0, 186234)\t0.2563610796533284\n",
      "  (1, 134809)\t0.45558845297596706\n",
      "  (1, 414813)\t0.27239375355613027\n",
      "  (1, 414814)\t0.27239375355613027\n",
      "  (1, 358360)\t0.3969987319130449\n",
      "  (1, 255348)\t0.37645194070392657\n",
      "  (1, 275868)\t0.2910493007823228\n",
      "  (1, 334478)\t0.2998095779604261\n",
      "  (1, 344098)\t0.3716485253158966\n",
      "  (1, 158085)\t0.17313454922446697\n",
      "  (1, 159634)\t0.04499681916006078\n",
      "  (2, 279551)\t0.9081978655905243\n",
      "  (2, 294639)\t0.40881616028062795\n",
      "  (2, 159634)\t0.0896994093080883\n",
      "  (3, 8825)\t0.6835926384080803\n",
      "  (3, 106530)\t0.47601062669803396\n",
      "  (3, 320551)\t0.2548963104019051\n",
      "  (3, 195064)\t0.2528504044731518\n",
      "  (3, 214218)\t0.4155130879671634\n",
      "  (3, 159634)\t0.06751596562351815\n",
      "  (4, 298891)\t0.5045028728603181\n",
      "  (4, 284517)\t0.4890714618003977\n",
      "  :\t:\n",
      "  (336365, 132849)\t0.4611469630308809\n",
      "  (336365, 306776)\t0.3144068153801051\n",
      "  (336365, 289741)\t0.2887249648566921\n",
      "  (336365, 289633)\t0.2982745881271165\n",
      "  (336365, 159634)\t0.059261764349843364\n",
      "  (336366, 227987)\t0.49763932525257976\n",
      "  (336366, 164940)\t0.5080781576579648\n",
      "  (336366, 328042)\t0.5713382416667517\n",
      "  (336366, 195928)\t0.4026973705766959\n",
      "  (336366, 159634)\t0.07496084986714655\n",
      "  (336367, 407230)\t0.9951579976685231\n",
      "  (336367, 159634)\t0.09828814616410146\n",
      "  (336368, 107886)\t0.655579505408524\n",
      "  (336368, 385941)\t0.49078393832101486\n",
      "  (336368, 208488)\t0.47073149189377866\n",
      "  (336368, 322924)\t0.321816780650776\n",
      "  (336368, 159634)\t0.06474921007593132\n",
      "  (336369, 368528)\t0.9951579976685231\n",
      "  (336369, 159634)\t0.09828814616410146\n",
      "  (336370, 389097)\t0.4862360824137861\n",
      "  (336370, 386802)\t0.531272802037052\n",
      "  (336370, 196849)\t0.5530183264823784\n",
      "  (336370, 419045)\t0.28473668752542786\n",
      "  (336370, 292607)\t0.2991473282437741\n",
      "  (336370, 159634)\t0.0702161472232794\n"
     ]
    }
   ],
   "source": [
    "# Split into training and testing dataset 80:20 ratio\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "print(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "226702    good\n",
      "370689    good\n",
      "304005    good\n",
      "235092    good\n",
      "293973    good\n",
      "          ... \n",
      "259178    good\n",
      "365838    good\n",
      "131932    good\n",
      "146867    good\n",
      "121958    good\n",
      "Name: label, Length: 336371, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Training the Logistic Regression model on the Training set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
       "                   multi_class='warn', n_jobs=None, penalty='l2',\n",
       "                   random_state=42, solver='warn', tol=0.0001, verbose=0,\n",
       "                   warm_start=False)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Model Building using logistic regression\n",
    "\n",
    "classifier = LogisticRegression(random_state = 42)\n",
    "classifier.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Predicting the Test set results & Making the Confusion Matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Confusion Matrix of the model is:  [[12367  2597]\n",
      " [  377 68752]]\n",
      "Accuracy of our model is:  0.9646343928745555\n"
     ]
    }
   ],
   "source": [
    "y_pred = classifier.predict(X_test)\n",
    "from sklearn.metrics import confusion_matrix, accuracy_score \n",
    "\n",
    "#Confusion Matrix of the Model\n",
    "\n",
    "print(\"Confusion Matrix of the model is: \",confusion_matrix(y_test, y_pred))\n",
    "\n",
    "# Accuracy of the Model\n",
    "\n",
    "print(\"Accuracy of our model is: \",accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualising the Training set results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "label=[\"good\",\"bad\"]\n",
    "index_y = np.arange(len(label))\n",
    "#sample=np.arange(len(y_train))\n",
    "index_X=[0,0]\n",
    "for i in y_train:\n",
    "    if(i=='good'):\n",
    "        index_X[0] = index_X[0]+1\n",
    "    else:\n",
    "        index_X[1] = index_X[1]+1\n",
    "#print(sample)\n",
    "#print(index_y)\n",
    "#print(index_X)\n",
    "plt.bar(index_y, index_X)\n",
    "plt.xlabel('Class', fontsize=10)\n",
    "plt.ylabel('No of URL', fontsize=10)\n",
    "plt.xticks(index_y, label, fontsize=10, rotation=15)\n",
    "plt.title('MALACIOUS URL DETECTION [Training Set]')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualising the Test set results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "label=[\"good\",\"bad\"]\n",
    "index_y = np.arange(len(label))\n",
    "sample=np.arange(len(y_test))\n",
    "index_X=[0,0]\n",
    "for i in y_test:\n",
    "    if(i=='good'):\n",
    "        index_X[0] = index_X[0]+1\n",
    "    else:\n",
    "        index_X[1] = index_X[1]+1\n",
    "#print(sample)\n",
    "#print(index_y)\n",
    "#print(index_X)\n",
    "plt.bar(index_y, index_X)\n",
    "plt.xlabel('Class', fontsize=10)\n",
    "plt.ylabel('No of URL', fontsize=10)\n",
    "plt.xticks(index_y, label, fontsize=10, rotation=15)\n",
    "plt.title('MALACIOUS URL DETECTION [Test Set]')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
