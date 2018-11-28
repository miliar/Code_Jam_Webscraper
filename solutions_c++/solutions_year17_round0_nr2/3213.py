#include<cstdio>
#include<cstring>

void set_all_nines(char* number, size_t start, size_t end) {
    for (size_t i = start; i < end; ++i) {
        number[i] = '9';
    }
}

int main() {
    int t;
    scanf("%d", &t);
    int case_no = 0;
    char number[20];
    do {
        ++case_no;
        scanf("%19s", number);
        size_t len = strlen(number);
        if (len > 1) {
            size_t last_decrementable = 0;
            size_t first_wrong = 0;
            for (size_t i = 1; i < len; ++i) {
                if (number[i-1] > number[i]) {
                    first_wrong = i;
                    break;
                }
                if (number[i] > '0' && number[i] > number[i - 1])
                    last_decrementable = i;
            }
            if (first_wrong > 0) {
                if (last_decrementable > 0 || number[0] > '1') {
                    --number[last_decrementable];
                    set_all_nines(number, last_decrementable + 1, len);
                } else {
                    set_all_nines(number, 0, len - 1);
                    number[len - 1] = '\0';
                }
            }
        }
        printf("Case #%d: %s\n", case_no, number);
    } while (case_no != t);
    return 0;
}
