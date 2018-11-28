#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 20;

int T, test_case = 1;
char input[MAXN];

int get_untidy_index() {
  for (int i = 0; i + 1 < strlen(input); ++i) {
    if (input[i] > input[i + 1]) {
      return i; 
    }
  }
  return -1;
}

void set_nines_from(int idx) {
  for (int i = idx; i < strlen(input); ++i) {
    input[i] = '9';
  }
}

int main(void) {
  scanf("%d", &T);

  while (T--) {
    scanf("%s", input);
   
    int untidy_idx;
    while ((untidy_idx = get_untidy_index()) != -1) {
      set_nines_from(untidy_idx + 1);
      input[untidy_idx] -= 1;
    }

    int leading_zeros = 0;
    while (input[leading_zeros] == '0') {
      leading_zeros++;
    }
    memcpy(input, input + leading_zeros, strlen(input) - leading_zeros + 1);

    printf("Case #%d: %s\n", test_case++, input);
  }
  return 0;
}
