#include <stdio.h>

unsigned long long int get_max_tidy_number(unsigned long long int number);
int is_tidy_number(unsigned long long int number);

int main(void) {

  int testcase = 0;
  unsigned long long result;
  unsigned long long input_number;
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &testcase);
  for( int test = 1; test <= testcase; test ++){
    scanf("%ld", &input_number);
    result = get_max_tidy_number(input_number);
    //printf("Case #%d: %llu\n", test, input_number);
    printf("Case #%d: %llu\n", test, result);
  }

  return 0;
}

unsigned long long int get_max_tidy_number(unsigned long long int number) {
  unsigned long long int offset = 1;
  unsigned long long int i =0;
  while (is_tidy_number(number) == 0) {
    for(i = 10; number/i != 0 ; i *= 10){
      if( number/i % 10 ==0){
        offset = number % i + 1;
        break;
      }
    }
    //offset = number % i + 1;
    number -= offset;
  }
  return number;
}

int is_tidy_number(unsigned long long int number) {
  int prev = -1, next = -1;
  unsigned long long int tidy_number = number;
  while( true ){
    prev = tidy_number % 10;
    next = tidy_number / 10 % 10;
    if( prev >= next ){
      tidy_number = tidy_number / 10;
      if( tidy_number <= 0 )
        return 1;
      else
        continue;
    }
    else
      return 0;
  }
}