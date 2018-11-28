#include <bits/stdc++.h>

int number[20];
int answer[20];
int len;

void recurse_create(int index, bool fall);

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; t++)
  {
    long long int N;
    scanf("%lld", &N);
    len = 0;
    while (N > 0)
    {
      number[len] = N % 10;
      N /= 10;
      len++;
    }
    recurse_create(0, false);
    long long int ans = 0;
    for (int i = 0; i < len; i++)
    {
      ans *= 10;
      ans += answer[i];
    }
    printf("Case #%d: %lld\n", t + 1, ans);
  }
}

void recurse_create(int index, bool fall)
{
  if (index >= len)
  {
    return;
  }
  if (fall)
  {
    answer[index] = 9;
    return recurse_create(index + 1, fall);
  }
  int i = index;
  bool flag = false;
  while (i < len)
  {
    if (number[(len - index - 1)] < number[(len - i - 1)])
    {
      break;
    }
    if (number[(len - index - 1)] > number[(len - i - 1)])
    {
      flag = true;
      break;
    }
    i++;
  }
  if (flag)
  {
    answer[index] = number[(len - index - 1)] - 1;
    recurse_create(index + 1, true);
  }
  else
  {
    answer[index] = number[(len - index - 1)];
    recurse_create(index + 1, false);
  }
}