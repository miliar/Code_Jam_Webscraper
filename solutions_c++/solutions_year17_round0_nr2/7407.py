#include <cstdio>

using namespace std;

int main() {

    int T; scanf("%d", &T); 

    for (int test = 1; test <= T; ++test) {

        char number[20];
        scanf("%s", number);

        for (int i = 0; number[i+1] != 0; ++i) {
            if (number[i+1] < number[i]) {
               
                char digit = number[i];
                int start = i;

                while ((start > 0) && (number[start] == digit)) --start;

                if (number[start] != digit) ++start;

                --number[start];

                for (int j = start + 1; number[j] != 0; ++j) {
                    number[j] = '9';
                }

                break;
            }
        }

        printf("Case #%d: ", test);
        
        if (number[0] == '0') printf("%s\n", number + 1);
        else printf("%s\n", number);

    }

    return 0;
}
