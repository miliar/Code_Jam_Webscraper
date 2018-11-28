#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_tidy(char *number, int length)
{
  int digit = number[0];
  for (int i = 0; i < length; i++) {
    if (number[i] >= digit){
      digit = number[i];
      continue;
    }
    return 0;
  }
  return 1;
}

char * remove_leading_zeros(char *number, int length)
{
  for (int i = 0; i < length; i++) {
    if (*number == '0') {
      number++;
    } else{
      break;
    }
  }
  return number;
}

int find_pivot(char *number, int length) //first lower digit
{
  int digit = 0;
  int index = -1;
  for (int i = 0; i < length; i++) {
    if (number[i] >= digit){
      digit = number[i];
      continue;
    }
    index = i;
    break;
  }

  return index;
}

void trunk_since_pivot(char *number, int length, int pivot)
{
  for (int i = pivot; i < length; i++) {
    number[i] = '9';
  }
}

void minus_one_at(char * number, int length, int pivot){
  int start = pivot-1;
  for (int i = start; i >= 0; i--) {
    char digit = number[i]-1;
    if (digit <= '0' && i != 0){
      number[i] = '9';
    } else {
      number[i] = digit;
      break;
    }
  }
}

char * get_last_tidy(char *number, int length)
{
  //printf("%s\n",number);
  if (is_tidy(number, length)) return number;

  while (!is_tidy(number, length)) {
    int pivot = find_pivot(number, length);
    trunk_since_pivot(number, length, pivot);
    //printf("%s\n",number);
    minus_one_at(number, length, pivot);
    //printf("%s\n",number);
  }

  return number;
}

int main()
{
  int t_cases;
  scanf("%d\n",&t_cases);

  for (int i = 0; i < t_cases; i++) {
    char number[20];
    scanf("%s\n",number);
    int length = strlen(number);
    char *last_tidy = get_last_tidy(number, length);

    last_tidy = remove_leading_zeros(last_tidy, strlen(last_tidy));
    printf("Case #%d: %s\n",i+1,last_tidy);
  }

  return 0;
}
