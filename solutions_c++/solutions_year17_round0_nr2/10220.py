#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;

#define vi vector<int>
#define pii pair<int,int>
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)


bool tidy(ll k)
{

    string str;
    ostringstream temp;
    temp<<k;
    str=temp.str();

    int l=str.size();
    for(int i=1;i<l;i++){
        int a=(str[i-1] - '0');
        int b=(str[i] - '0');
        if(b<a){
            return false;
        }
    }
    return true;
}
int entier(int k){

    for(ll i=k;i>=1;i--){
            if(tidy(i))
            return i;
        }

}
int T;
ll K,r;
int main()
{
      #define small

   #ifdef small
    freopen("B-small-attempt0.in","rt",stdin);
    freopen("A.txt","wt",stdout);
    scanf("%d",&T);

    for(int i=1;i<=T;i++){
        cin>>K;
        if(K%10 == K){
            r=K;
        }
        else{
           r=entier(K);
        }

       printf("Case #%d: %d \n",i,r);
    }


   #endif

   #ifdef large
   freopen("A-small.in","rt",stdcin);
    freopen("A.out","wt",stdout);
   #endif
    return 0;
}
