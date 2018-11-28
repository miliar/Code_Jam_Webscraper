//============================================================================
// Name        : CPP-Scratchpad.cpp
// Author      : Simon Redman <simon@ergotech.com>
// Version     :
// Copyright   : 
// Description : Throwaway scratchpad. Pay no mind.
//============================================================================

#include <cstdlib>
#include <iostream>
#include <fstream> // Required for fast stdin readers

//typedef __int128 int128_t;

//typedef unsigned __int128 uint128_t;

/**
 * Super fast input parser from: http://stackoverflow.com/a/27999517/3723163
 * Reads char values directly from the input stream. Assumes they are only base10 digits.
 */
static size_t parseInt ()
{
  size_t toReturn;
  int c;

  // Get the first digit. This deals with weird line endings
  while (!isdigit(toReturn = getchar_unlocked()))
    ;

  toReturn = toReturn - '0';
  while (isdigit(c = getchar_unlocked()))
  {
    toReturn = 10 * toReturn + (c - '0');
  }

  return toReturn;
}

#define MAX_STRING_LENGTH 18

/**
 * Similar to above, but leaves each digit in its own char array
 * Useful for exactly this problem and probably no other..
 * Output is stored in the passed array.
 * Returns the number of digits read
 */
static inline size_t parseIntCharArray (char output[MAX_STRING_LENGTH])
{
  size_t index;

  char digit;

  // Get the first digit. This deals with weird line endings
  while (!isdigit(digit = getchar_unlocked()))
    ;

  output[0] = digit - '0';
  for (index = 1; index < MAX_STRING_LENGTH; index++)
  {
    digit = getchar_unlocked();

    if (isdigit(digit))
    {
      output[index] = digit - '0';
    } else
    {
      break;
    }
  }
  size_t toReturn = index;

  // Flip the array so as not to be a jerk
  for (index = 0; index < (toReturn + 1) / 2; index++)
  {
    char temp = output[index];
    output[index] = output[toReturn - 1 - index];
    output[toReturn - 1 - index] = temp;
  }

  return toReturn;
}

/**
 * Read characters off of stdin until we get a character that is not a letter
 */
static std::string parseString ()
{
  // TODO: This seems to cause timeouts in Kattis!!!
  char currentChar;
  size_t length = 0; // Current length of the string
  // Add one for null terminator
  static char *toReturn = new char[MAX_STRING_LENGTH + 1];

  currentChar = getchar_unlocked();
  // Spin loop to not get garbage
  while (!((currentChar >= 'a' && currentChar <= 'z') || (currentChar >= 'A' && currentChar <= 'Z')))
  {
    if (currentChar == EOF)
    {
      toReturn[length] = 0;
      return std::string(toReturn);
    }
    currentChar = getchar_unlocked();
  }
  while ((currentChar >= 'a' && currentChar <= 'z') || (currentChar >= 'A' && currentChar <= 'Z'))
  {
    toReturn[length] = currentChar;
    length++;
    currentChar = getchar_unlocked();
  }
  toReturn[length] = 0;
  return std::string(toReturn);
}

/**
 * Solver for Google Code Jam 2017 Round 1 Question 2
 */
int main ()
{
  size_t index;
  size_t jdex;

  size_t num_tests = parseInt();

  // Maximum input is 10^18 ~= 2^60

  for (index = 0; index < num_tests; index++)
  {
    char digits[18];
    char myDigits[18];
    size_t numDigits = parseIntCharArray(digits);

    for (jdex = 0; jdex < numDigits - 1; jdex++)
    {
      myDigits[jdex] = 9;
    }

    myDigits[numDigits - 1] = digits[numDigits - 1];

    // Start at 1 because I don't want to touch the top value if possible
    for (jdex = 1; jdex < numDigits; jdex++)
    {
      size_t thisIndex = numDigits - jdex - 1;

      char thisDigit = digits[thisIndex];
      char nextDigit = digits[thisIndex + 1];

      if (thisDigit >= nextDigit)
      {
        myDigits[thisIndex] = thisDigit;
      } else
      {
        myDigits[thisIndex + 1]--;
        if (numDigits < 3)
        {
          break;
        }
        // Fix digits
        size_t kdex;
        for (kdex = thisIndex + 1; kdex < numDigits; kdex++)
        {
          char thisDigit = myDigits[kdex];
          char nextDigit = myDigits[kdex + 1];

          if (nextDigit > thisDigit)
          {
            myDigits[kdex] = 9;
            myDigits[kdex + 1]--;
          } else
          {
            break;
          }
        }
        break;
      }
    }

    size_t output = 0;
    for (jdex = 0; jdex < numDigits; jdex++)
    {
      output = output * 10 + myDigits[numDigits - 1 - jdex];
    }
    std::cout << "Case #" << index + 1 << ": " << output << std::endl;
  }

}
