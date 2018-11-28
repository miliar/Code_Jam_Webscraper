#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

const unsigned MAXDIGIT = 18;
const char ZERO = '0';
const char NINE = '9';

unsigned notTidy(char *num)
{
  unsigned len;
  len = strlen(num);
  char d1[2];
  char d2[2];
  d1[1] = 0;
  d2[1] = 0;
  for (unsigned i = 1; i < len; i++){
    d2[0] = num[i];
    d1[0] = num[i - 1];
    if (atoi(d2) < atoi(d1))
      return i;
  }
  return 0;
}

char dec(const char digit)
{
  if (digit == ZERO)
    return '9';
  else
    return digit - 1;
}

void dec(char *num)
{
  unsigned len = strlen(num);
  unsigned i;
  for (i = len - 1; i >= 0; i--){
    num[i] = dec(num[i]);
    if (num[i] != NINE)
      break;
  }
  if (num[0] == ZERO){
    for (i = 0; i < len - 1; i++)
      num[i] = num[i + 1];
    num[i] = 0;
  }
}

void tidy(char *num, unsigned bad)
{
  unsigned len = strlen(num);
  unsigned i;
  for (i = len - 1; i >= bad; i--){
    num[i] = NINE;
  }
  num[bad - 1] = dec(num[bad - 1]);
  if (num[0] == ZERO){
    for (i = 0; i < len - 1; i++)
      num[i] = num[i + 1];
    num[i] = 0;
  }
}

int main()
{
  unsigned T, t;
  cin >> T;
  char num[MAXDIGIT + 1];
  unsigned bad;
  for (t = 1; t <= T; t++){
    scanf("%s", &num);
    while ((bad = notTidy(num)) > 0)
      tidy(num, bad);
    cout << "Case #" <<  t << ": " << num << endl;
  }
}
