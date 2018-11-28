/*
 Problem name :
 Problem link :
 Category :
 Algorithm :
 Comment : Whenever you start to believe  yourself, people also start to believe in you
 Date : 08-Apr-2017
 Verdict :
*/

#include<bits/stdc++.h>

#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<deque>
#include<functional>
#include<string>
#include<iostream>
#include<cctype>
#include<set>
#include<climits>
#include<iomanip>
#include<cassert>
#include<sstream>


#define pb              push_back
#define ppb             pop_back
#define lcm(x,y)        (abs(x) /gcd(x,y))* abs(y)
#define sq(x)          ( (x)* (x) )
#define check(x,w)      (x&(1<<w))
#define pause           system("pause");
#define pf              printf
#define sf              scanf

#define F               first
#define S               second
#define AND             &&
#define OR              ||
#define NOT             ~
#define XOR             ^
#define PI              acos(-1.0)
#define EPS             1e-8
#define INF             1e9
#define MIN(a,b)        ((a)<(b)?(a):(b))
#define MAX(a,b)        ((a)>(b)?(a):(b))
#define MOD(x,y)        (((x)*(y))%mod)
#define ODD(x)          (((x)&1)==0?(0):(1))
#define ALL(x)          (x).begin(),(x).end()




using namespace std;
int main(int argc, char *argv[])
{
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("probelmA.txt","w",stdout);

    int t;
    int k;
    string str;
    cin>>t;
    for(int m=1;m<=t;m++)
    {
        cin>>str;
        cin>>k;
        bool flip = false;
        int contain = 0;
        for(int i = 0; i <=str.length()-k; i++)
        {
            if(str[i] == '-')
            {
                for(int j = i; j <k+i; j++)
                {
                    if(str[j] == '-') str[j] = '+';
                    else str[j] = '-';
                }
                contain++;
            }
        }
        flip = false;
        for(int i = 0; i<str.length(); i++)
        {
            if(str[i] == '-')
            {
                flip = true;
                cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
                break;
            }
        }
        if(!flip)
            cout<<"Case #"<<m<<": "<<contain<<endl;
    }
    return 0;
}
