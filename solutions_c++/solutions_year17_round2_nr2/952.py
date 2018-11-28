#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

int T;

int N, R, O, Y, G, B, V;
vector<char> vecF, vecS, vecT, result;

void output(char first, int first_remain, int first_extra, char second, int second_remain, int second_extra, char third, int third_remain, int third_extra)
{
    if (first_extra > 0) {
        char extra = first == 'R' ? 'G' : (first == 'Y' ? 'V' : 'O');
        for (int i = 0; i < first_extra; ++i) {
            vecF.push_back(first);
            vecF.push_back(extra);
        }
        vecF.push_back(first);
    }
    if (second_extra > 0) {
        char extra = second == 'R' ? 'G' : (second == 'Y' ? 'V' : 'O');
        for (int i = 0; i < second_extra; ++i) {
            vecS.push_back(second);
            vecS.push_back(extra);
        }
        vecS.push_back(second);
    }
    if (third_extra > 0) {
        char extra = third == 'R' ? 'G' : (third == 'Y' ? 'V' : 'O');
        for (int i = 0; i < third_extra; ++i) {
            vecT.push_back(third);
            vecT.push_back(extra);
        }
        vecT.push_back(third);
    }
    int ff = first_extra > 0 ? first_remain + 1 : first_remain;
    int ss = second_extra > 0 ? second_remain + 1 : second_remain;
    int tt = third_extra > 0 ? third_remain + 1 : third_remain;
    //cout << "size: " << vecF.size() << ", " << vecS.size() << ", " << vecT.size() << endl;
    vector<char> temp;
    int diff = ss + tt -ff;
    //cout << ff << ", " << ss << ", " << tt << ", " << diff << endl;
    if (diff % 2 == 0) {
        if (ss >= tt) {
            for (int i = 0; i < diff/2; ++i) {
                temp.push_back(second);
                temp.push_back(third);
            }
            ss -= diff/2;
            tt -= diff/2;
            while(ss-- > 0) {
                temp.push_back(second);
                temp.push_back(first);
            }
            while(tt-- > 0) {
                temp.push_back(third);
                temp.push_back(first);
            }
        } else {
            for (int i = 0; i < diff/2; ++i) {
                temp.push_back(third);
                temp.push_back(second);
            }
            ss -= diff/2;
            tt -= diff/2;
            while(tt-- > 0) {
                temp.push_back(third);
                temp.push_back(first);
            }
            while(ss-- > 0) {
                temp.push_back(second);
                temp.push_back(first);
            }
        }
    } else {
        if (ss >= tt) {
            for (int i = 0; i < diff/2 + 1; ++i) {
                temp.push_back(second);
                temp.push_back(third);
            }
            ss -= (diff/2 + 1);
            tt -= (diff/2 + 1);
            temp.push_back(first);
            while(ss-- > 0) {
                temp.push_back(second);
                temp.push_back(first);
            }
            while(tt-- > 0) {
                temp.push_back(third);
                temp.push_back(first);
            }
        } else {
            for (int i = 0; i < diff/2 + 1; ++i) {
                temp.push_back(third);
                temp.push_back(second);
            }
            ss -= (diff/2 + 1);
            tt -= (diff/2 + 1);
            temp.push_back(first);
            while(tt-- > 0) {
                temp.push_back(third);
                temp.push_back(first);
            }
            while(ss-- > 0) {
                temp.push_back(second);
                temp.push_back(first);
            }

        }
    }

    int size = temp.size();
    //cout << "temp size: " << size << endl;
    for (int i = 0; i < size; ++i) {
        if (temp[i] == first && !vecF.empty()) {
            for (int j = 0; j < vecF.size(); ++j) {
                result.push_back(vecF[j]);
            }
            vecF.clear();
            continue;
        }
        if (temp[i] == second && !vecS.empty()) {
            for (int j = 0; j < vecS.size(); ++j) {
                result.push_back(vecS[j]);
            }
            vecS.clear();
            continue;
        }
        if (temp[i] == third && !vecT.empty()) {
            for (int j = 0; j < vecT.size(); ++j) {
                result.push_back(vecT[j]);
            }
            vecT.clear();
            continue;
        }
        result.push_back(temp[i]);
    }
    temp.clear();

    for (int i = 0; i < result.size(); ++i) {
        printf("%c", result[i]);
    }
    printf("\n");
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("result.out", "w", stdout);
    scanf("%d", &T);
    int t = 1;
    while(t <= T)
    {
        vecF.clear();
        vecS.clear();
        vecT.clear();
        result.clear();
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

        printf("Case #%d: ", t++);
        bool possible = true;

        if (possible) {
            if (N > R + G) {
                if (G > 0)
                    R -= (G + 1);
            } else {
                if (R == G) {
                    for (int i = 0; i < G; ++i) {
                        printf("RG");
                    }
                    printf("\n");
                    continue;
                } else {
                    possible = false;
                }
            }
            if (R < 0) {
                possible = false;
            }
        }

        if (possible) {
            if (N > Y + V) {
                if (V > 0)
                    Y -= (V + 1);
            } else {
                if (Y == V) {
                    for (int i = 0; i < V; ++i) {
                        printf("YV");
                    }
                    printf("\n");
                    continue;
                } else {
                    possible = false;
                }
            }
            if (Y < 0) {
                possible = false;
            }
        }

        if (possible) {
            if (N > B + O) {
                if (O > 0)
                    B -= (O + 1);
            } else {
                if (B == O) {
                    for (int i = 0; i < O; ++i) {
                        printf("BO");
                    }
                    printf("\n");
                    continue;
                } else {
                    possible = false;
                }
            }
            if (B < 0) {
                possible = false;
            }
        }

        int extraR = G > 0 ? 1 : 0;
        int extraY = V > 0 ? 1 : 0;
        int extraB = O > 0 ? 1 : 0;
        char first, second, third;
        int first_remain, first_extra, second_remain, second_extra, third_remain, third_extra;

        if (possible) {
            if (R >= Y) {
                if (Y >= B) {
                    first = 'R';
                    second = 'Y';
                    third = 'B';
                    first_remain = R;
                    first_extra = G;
                    second_remain = Y;
                    second_extra = V;
                    third_remain = B;
                    third_extra = O;
                    if (R + extraR > B + Y + extraB + extraY) {
                        possible = false;
                    }
                } else if (R >= B){
                    first = 'R';
                    second = 'B';
                    third = 'Y';
                    first_remain = R;
                    first_extra = G;
                    second_remain = B;
                    second_extra = O;
                    third_remain = Y;
                    third_extra = V;
                    if (R + extraR > B + Y + extraB + extraY) {
                        possible = false;
                    }
                } else {
                    first = 'B';
                    second = 'R';
                    third = 'Y';
                    first_remain = B;
                    first_extra = O;
                    second_remain = R;
                    second_extra = G;
                    third_remain = Y;
                    third_extra = V;
                    if (B + extraB > R + Y + extraR + extraY) {
                        possible = false;
                    }
                }
            } else {
                if (R >= B) {
                    first = 'Y';
                    second = 'R';
                    third = 'B';
                    first_remain = Y;
                    first_extra = V;
                    second_remain = R;
                    second_extra = G;
                    third_remain = B;
                    third_extra = O;
                    if (Y + extraY > R + B + extraR + extraB) {
                        possible = false;
                    }
                } else if (Y >= B) {
                    first = 'Y';
                    second = 'B';
                    third = 'R';
                    first_remain = Y;
                    first_extra = V;
                    second_remain = B;
                    second_extra = O;
                    third_remain = R;
                    third_extra = G;
                    if (Y + extraY > R + B + extraR + extraB) {
                        possible = false;
                    }
                } else {
                    first = 'B';
                    second = 'Y';
                    third = 'R';
                    first_remain = B;
                    first_extra = O;
                    second_remain = Y;
                    second_extra = V;
                    third_remain = R;
                    third_extra = G;
                    if (B + extraB > R + Y + extraR + extraY) {
                        possible = false;
                    }
                }
            }
        }
        //cout << "poss: " << possible << endl;
        //cout << "sort: " << first << ", " << second << ", " << third << endl;
        //cout << first_remain << ", " << first_extra << ", " << second_remain << ", " << second_extra << ", " << third_remain << ", " << third_extra << endl;

        if (!possible)
            printf("IMPOSSIBLE\n");
        else {
            output(first, first_remain, first_extra, second, second_remain, second_extra, third, third_remain, third_extra);
        }
    }
    return 0;
}
