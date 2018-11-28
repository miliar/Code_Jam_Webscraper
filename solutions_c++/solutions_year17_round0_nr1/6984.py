#include <iostream>
#include <vector>

int main(int argc, char *argv[])
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int test_case_number;
    scanf("%d", &test_case_number);
    for (int test_case = 1; test_case <= test_case_number; test_case++) {
        std::string s;
        int k;
        std::cin >> s;
        scanf("%d", &k);
        std::vector<int> values(s.size());
        for (size_t i = 0; i < s.size(); i++) {
            if (s[i] == '+') {
                values[i] = +1;
            } else if (s[i] == '-') {
                values[i] = -11;
            }
        }

        int answer = 0;
        for (int i = 0; i + k - 1 < values.size(); i++) {
//            std::cout << i << " " << s << std::endl;
            if (s[i] == '+') {
                continue;
            } else {
                answer++;
                for (int j = i; j < i + k; j++) {
                    if (s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }
            }

        }

        int id = s.size() - k + 1;
        for (int i = id;  i < s.size(); i++) {
            if (s[i] == '-') {
                answer = -1;
                break;
            }
        }
        if (answer == -1) {
            printf("Case #%d: IMPOSSIBLE\n", test_case);
        } else {
            printf("Case #%d: %d\n", test_case, answer);
        }
    }

    return 0;
}
