#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <time.h>
#include <vector>
#include <map>
#include <set>
#include <list>
#define pb push_back
#define ll long long
#define mp make_pair
#define pll pair<long,long>
#define plll pair<long,long>
#define F first
#define S second
#define INF 1000000000
#define MAXN 100500*4

using namespace std;


long m[1005000];

int main()
{
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    long n;
    cin>>n;
    for(int i=0;i<n;i++){
        long k,p;
        cout<<"Case #"<<i+1<<": ";
        cin>>k>>p;
        for(int j=0;j<1001500;j++){
            m[j] = 0;
        }
        m[k] = 1;
        for(int j=1000100;j>=0;j--){
            if(m[j]>0){
                p-=m[j];
                if(p<=0){
                    if(j%2==1){
                        cout<<j/2<<' '<<j/2<<endl;
                    } else{
                        cout<<j/2<<' '<<j/2-1<<endl;
                    }
                    break;
                }
                if(j%2==1){
                    m[j / 2] += m[j] * 2;
                } else{
                    m[j / 2 - 1] += m[j];
                    m[j / 2] += m[j];
                }

            }
        }
    }
    return 0;
}
