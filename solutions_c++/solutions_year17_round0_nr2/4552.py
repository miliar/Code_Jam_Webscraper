#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <bits/stdc++.h>

using namespace std;
using namespace __gnu_pbds;

typedef long long LL;

typedef tree<
    int,
    null_type,
    less<int>,
    rb_tree_tag,
    tree_order_statistics_node_update>
ordered_set;
//find_by_order
//order_of_key

#define FO(i,a,b) for (int i = (a); i < (b); i++)

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );
#define ALL(v) v.begin(),v.end()

#define X first
#define Y second
#define MP make_pair

typedef pair<int,int> pint;
typedef map<int,int> mint;

void show() {cout<<'\n';}
template<typename T,typename... Args>
void show(T a, Args... args) { cout<<a<<" "; show(args...); }
template<typename T>
void show_c(T& a) { for ( auto &x:a ){ cout<<x<<" ";}cout<<endl;  }



string calc(string str) {
    int pos = -1;
    for (int i=str.length()-1; i-1>=0; --i) {
        if (str[i-1] > str[i]) {
            pos = i;
            break;
        }
    }
    if (pos == -1) {
        return str;
    }

    LL A;
    sscanf(str.substr(0,pos).c_str(), "%lld", &A);
    int len = str.substr(pos).length();

    A--;
    char tmp[25];
    sprintf(tmp, "%lld", A);
    string res = calc(tmp);
    while ( len-- ){
        res += "9";
    }

    return res;
}


int main(){

    freopen("B-large.in","r",stdin);
    freopen("outB.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk) {
        string str;
        cin>>str;

        LL ans;
        sscanf(calc(str).c_str(), "%lld", &ans);

        printf("Case #%d: %lld\n", kk, ans);


    }


    return 0;
}
