#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <math.h>
#include <cstdlib>
#include <ctime>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "B"

int main()
{
//	freopen(QX ".txt","r",stdin);
	freopen(QX "-small-attempt0.in","r",stdin);freopen(QX "-small-attempt0.out","w",stdout);
//	freopen(QX "-small-attempt1.in","r",stdin);freopen(QX "-small-attempt1.out","w",stdout);
//	freopen(QX "-large.in","r",stdin);freopen(QX "-large.out","w",stdout);
//	freopen(QX "-large-practice.in","r",stdin);freopen(QX "-large-practice.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        int N,C,M;
        cin>>N>>C>>M;
        if (C != 2) {
            cout<<"!!!wrong input"<<endl;
        }
        int X[2][1000];
        cl(X,0);
        rep(i,M) {
            int p,b;
            cin>>p>>b;
            X[b-1][p-1]++;
        }

        int y = 0, z = 0;
        int sum = 0;
        int sumX[2];
        cl(sumX, 0);
        rep(i,1000) {
            sum += X[0][i] + X[1][i];
            int y0 = sum/(i+1);
            y = max(y,y0);
            sumX[0] += X[0][i];
            sumX[1] += X[1][i];
        }
        y = max(y,max(sumX[0],sumX[1]));

        rep(i,1000) {
            int t = X[0][i] + X[1][i];
            if (t > y) {
                z += t - y;
            }
        }

        // output
        cout << "Case #"<<caseId<<": "<<y<<" "<<z<<endl;
        //printf("Case #%d: %.8f\n",caseId,t);
	}
    return 0;
}
