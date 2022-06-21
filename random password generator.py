{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "623ee1a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "#A function do shuffle all the characters of a string\n",
    "def shuffle(string):\n",
    "  tempList = list(string)\n",
    "  random.shuffle(tempList)\n",
    "  return ''.join(tempList)\n",
    "\n",
    "#Main program starts here\n",
    "uppercaseLetter1=chr(random.randint(65,93)) #Generate a random Uppercase letter (based on ASCII code)\n",
    "uppercaseLetter2=chr(random.randint(65,93)) #Generate a random Uppercase letter (based on ASCII code)\n",
    "#Generate more characters here\n",
    "#....\n",
    "\n",
    "#Generate password using all the characters, in random order\n",
    "password = uppercaseLetter1 + uppercaseLetter2 # + ....\n",
    "password = shuffle(password)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7effbefc",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'rahil' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-0b25e3255a0a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mrahil\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'rahil' is not defined"
     ]
    }
   ],
   "source": [
    "rahil\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5e977401",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'YU'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7452afef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'YU'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5ce0a360",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'PASSWORD' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-e75fd8bfd5a4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mPASSWORD\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'PASSWORD' is not defined"
     ]
    }
   ],
   "source": [
    "PASSWORD"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "720f1bf5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'YU'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5d8460ab",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-8-97dd36d7725e>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-8-97dd36d7725e>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    password password\u001b[0m\n\u001b[1;37m             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "password password\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "adcf8cdb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'YU'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ab3f4201",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'JB'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6e1708a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'͵\\u0378'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "031fbc21",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ʙØ'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "29ab4a96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'çŒ'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e8c75e53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'`I'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a43f1571",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'GL'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3418eb87",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
