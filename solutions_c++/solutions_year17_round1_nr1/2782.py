// ConsoleApplication1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <stdlib.h>
#include <cmath>
#include <map>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;

int T;
int R,C;
char mp[35][35];
int lr[30][5];

void print(int n,int m) {
    for (int i = 0;i < n;i ++) {
        for (int j = 0;j < m;j ++) {
            putchar(mp[i][j]);
        }
        puts("");
    }
}
int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T;
    int CC = 1;
    while (T --) {
        cin >> R >> C;
        for (int i = 0;i < R;i ++) {
            scanf("%s",mp[i]);
        }
         memset(lr,0,sizeof(lr));
        for (int i = 0;i < 30;i ++) {
            lr[i][0] = 0x3f3f3f3f;
            lr[i][1] = -1;
            lr[i][2] = 0x3f3f3f3f;
            lr[i][3] = -1;
        }
        for (int i = 0;i < R;i ++) {
            for (int j = 0;j < C;j ++) {
                char ch = mp[i][j];
                int idx = 0;
                if (ch == '?') {
                    idx = 30;
                }
                else {
                    idx = ch - 'A';
                }
                if (idx != 30) {
                    lr[idx][0] = min(lr[idx][0],i);
                    lr[idx][1] = max(lr[idx][1],i);
                    lr[idx][2] = min(lr[idx][2],j);
                    lr[idx][3] = max(lr[idx][3],j);
                    lr[idx][4] = 1;
                }

            }
        }

        for (int i = 0;i < 30;i ++) {
            if (lr[i][4] == 1) {
                int xmin = lr[i][0];
                int xmax = lr[i][1];
                int ymin = lr[i][2];
                int ymax = lr[i][3];
                for (int j = xmin;j <= xmax;j ++) {
                    for (int k = ymin;k <= ymax;k ++) {
                        mp[j][k] = char('A' + i);
                    }
                }
            }
        }
       // print(R,C);
        for (int i = 0;i < 30;i ++) {
            if (lr[i][4] == 1) {
                int xmin = lr[i][0];
                int xmax = lr[i][1];
                int ymin = lr[i][2];
                int ymax = lr[i][3];
                //->
                for (int j = xmax + 1;j  < R;j ++) {
                    bool ok = true;
                    for (int k =  lr[i][2];k <=  lr[i][3];k ++) {
                        //cout << j
                        if (mp[j][k] == '?') {

                        }
                        else {
                            ok = false;
                        }
                    }
                    if (ok) {
                        for (int k = lr[i][2];k <=  lr[i][3];k ++) {
                            mp[j][k] = i + 'A';
                        }
                        lr[i][1] = j;
                    }
                    else {
                        break;
                    }
                }

                 for (int j = xmin - 1;j  >= 0;j --) {
                    bool ok = true;
                    for (int k = lr[i][2];k <= lr[i][3];k ++) {
                        if (mp[j][k] == '?') {

                        }
                        else {
                            ok = false;
                        }
                    }
                    if (ok) {
                        for (int k = lr[i][2];k <= lr[i][3];k ++) {
                            mp[j][k] = i + 'A';
                        }
                        lr[i][0] = j;
                    }
                    else {
                        break;
                    }
                }




            }
        }



          for (int i = 0;i < 30;i ++) {
            if (lr[i][4] == 1) {
                int xmin = lr[i][0];
                int xmax = lr[i][1];
                int ymin = lr[i][2];
                int ymax = lr[i][3];
                //->



                for (int j = ymax + 1;j  < C;j ++) {
                    bool ok = true;
                    for (int k = lr[i][0];k <= lr[i][1];k ++) {
                        if (mp[k][j] == '?') {

                        }
                        else {
                            ok = false;
                        }
                    }
                    if (ok) {
                        for (int k = lr[i][0];k <= lr[i][1];k ++) {
                            mp[k][j] = i + 'A';
                        }
                        lr[i][3] = j;
                    }
                    else {
                        break;
                    }
                }

                for (int j = ymin - 1;j  >= 0;j --) {
                    bool ok = true;
                    for (int k = lr[i][0];k <= lr[i][1];k ++) {
                           // cout << k << " " << j << endl;
                        if (mp[k][j] == '?') {
                          //  cout << k << " " << j << endl;
                        }
                        else {
                            ok = false;
                        }
                    }
                    if (ok) {
                        for (int k = lr[i][0];k <= lr[i][1];k ++) {
                            mp[k][j] = i + 'A';
                        }
                        lr[i][2] = j;
                    }
                    else {
                        break;
                    }
                }




            }
        }




        printf("Case #%d:\n",CC ++);
        print(R,C);
       // cout << 1 << endl;


    }

}


























































