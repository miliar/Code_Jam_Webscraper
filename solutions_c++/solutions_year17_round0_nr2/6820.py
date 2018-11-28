#include <cstdio>
#include <cstring>
#include <vector>

int main () {
    char buffer[2048];
    int t;
    std::vector<int> n;

    scanf("%d\n", &t);
    for(int i = 0; i < t; i++) {
        scanf("%s\n", buffer);
        for(int j = 0; j < strlen(buffer); j++) {
            n.push_back(buffer[j] - '0');
            //printf("%d", buffer[j] - '0');
        }
        //printf("\n");

        while(n.size() > 1) {
            int count = 1;
            for(auto digit = n.rbegin(); digit != n.rend(); ++digit) {
                auto next = digit + 1;
                if(*digit < *next) {
                    if(*next > 0) {
                        (*next)--;
                    } else {
                        count++;
                    }
                    for(int j = 0; j < count; j++) {
                        n.pop_back();
                    }
                    for(int j = 0; j < count; j++) {
                        n.push_back(9);
                    }
                    break;
                }
                count++;
            }

            while(n[0] == 0) {
                n.erase(n.begin());
            }

            /*for(auto digit = n.begin(); digit != n.end(); ++digit) {
                printf("%d", *digit);
            }
            printf("\n"); //*/

            if(count > n.size()) {
                break;
            }
        }

        printf("Case #%d: ", i + 1);
        for(auto digit = n.begin(); digit != n.end(); ++digit) {
            printf("%d", *digit);
        }
        printf("\n");

        n.clear();
    }

}