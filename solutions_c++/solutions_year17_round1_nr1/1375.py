#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int mmap[30][30];

int main()
{
    int test;
    while(scanf("%d", &test) == 1) {
        for(int l = 1; l <= test; ++l) {
            int r, c;
            scanf("%d %d", &r, &c);
            getchar();
            memset(mmap, 0, sizeof(mmap));
            char tmp, now;

            for(int i = 0; i < r; ++i) {
                tmp = '\0';
                for(int j = 0; j < c; ++j) {
                    scanf("%c", &now);
                    mmap[i][j] = now;
                    if(mmap[i][j] != '?') {
                        tmp = now;
                    } else if(tmp != '\0') {
                        mmap[i][j] = tmp;
                    }
                }
                getchar();

                for(int j = c-1; j >= 0; --j) {
                    if(mmap[i][j] != '?') tmp = mmap[i][j];
                    else if(tmp != '\0') mmap[i][j] = tmp;
                }
            }


            for(int j = 0; j < c; ++j) {
                tmp = '\0';
                for(int i = 0; i < r; ++i) {
                    if(mmap[i][j] != '?') {
                        tmp = mmap[i][j];
                    } else if(tmp != '\0')
                        mmap[i][j] = tmp;
                }

                for(int i = r-1; i >= 0; --i) {
                    if(mmap[i][j] != '?') {
                        tmp = mmap[i][j];
                    } else if(tmp != '\0')
                        mmap[i][j] = tmp;
                }
            }
            printf("Case #%d:\n", l);
            for(int i = 0; i < r; ++i) {
                for(int j = 0; j < c; ++j) printf("%c", mmap[i][j]);
                puts("");
            }
        }
        
    }

    return 0;
}