#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define all(a) (a.begin()),(a.end())
#define ZERO(a) meset(a,0,sizeof(a))
#define FOR(x,val,to) for(int x=(val);x<int((to));x++)
#define FORE(x,val,to) for(auto x=(val);x<=(to);x++)
#define FORR(x,arr) for(auto &x: arr)
#define FORRC(x,arr) for(auto const &x: arr)
#define PRINT(arr) {copy((arr).begin(), (arr).end(), ostream_iterator<int>(cout, " "));cout<<'\n';}
#define REE(s_) {cout<<s_<<'\n';return 0;} //print s_ and terminate program
#define GETVEC(vec,amount) copy_n(istream_iterator<int>(cin),(n),back_inserter((vec)))
#define GET(arr) for(auto &i: (arr)) cin>>i
#define INF 2139062143 //127 in memset -> memset(arr,127,size)
#define SINF 1061109567 //Safe INF, for graphs or 2d arrays 63 in memset(arr,63,size)
#define LL_INF 7234017283807667300 //100 in memset(arr,100,size) !!!must be LL
#define whatis(x) cerr << #x << " is " << x << endl;
#define s second
#define f first
typedef std::pair<int,int> pi;
typedef std::vector<int> vi;
typedef std::vector<std::string> vs;
typedef std::vector<long long> vll;
typedef std::vector<std::vector<int> > vvi;
using namespace std;

template<class T> ostream& operator<<(ostream &os, vector<T> V) {
  os<<"[";for(auto const &vv:V)os<<vv<<","; os<<"]";
  return os;
}
template<class L, class R> ostream& operator<<(ostream &os, pair<L, R> P) {
  os<<"("<<P.first<<","<<P.second<<")";
  return os;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n,t,k;
    cin >> t;
    FORE(i,1,t){
        cin >> n >> k;
        vector<pair<bool,tuple<int,int,int>>> vec(n,{0,{INF,INF,INF}});
        for(int x = 0, val = 0; x < n; ++x, ++val){
            if(val < get<0>(vec[x].s)){
                get<0>(vec[x].s) = val;
                get<2>(vec[x].s) = min(val,get<1>(vec[x].s));
            }
        }
        for(int x = n-1, val = 0; x >= 0; --x, ++val){
            if(val < get<1>(vec[x].s)){
                get<1>(vec[x].s) = val;
                get<2>(vec[x].s) = min(val,get<0>(vec[x].s));
            }
        }
        vector<pair<bool,tuple<int,int,int>>>::iterator elem;
        while(k--){
            vector<vector<pair<bool,tuple<int,int,int>>>::iterator> arr;
            int ans = -1;
            for(auto x=vec.begin(); x != vec.end(); ++x){
                if(!(x->f)){
                    if(get<2>(x->s) > ans){
                        arr = {x};
                        ans = get<2>(x->s);
                    }
                    else if(get<2>(x->s) == ans)
                        arr.pb(x);
                }
            }
            ans = -1;
            if(arr.size() > 1){
                vector<vector<pair<bool,tuple<int,int,int>>>::iterator> newarr;
                for(auto x=arr.begin(); x != arr.end(); ++x){
                    int tmp = max(get<0>((*x)->second),get<1>((*x)->second));
                    if(tmp > ans){
                        newarr = {*x};
                        ans = tmp;
                    }
                    else if(tmp == ans)
                        newarr.pb(*x);
                }
                elem = newarr.front();
            }
            else
                elem = arr.front();
            elem->first = 1;
            //cout << distance(vec.begin(),elem) << endl;
            for(int x = distance(vec.begin(),elem)+1, val = 0; x < n; ++x, ++val){
                if(vec[x].f == 0 && (val < get<0>(vec[x].s))){
                    get<0>(vec[x].s) = val;
                    get<2>(vec[x].s) = min(val,get<1>(vec[x].s));
                }
            }
            for(int x = distance(vec.begin(),elem)-1, val = 0; x >= 0; --x, ++val){
                if(vec[x].f == 0 && (val < get<1>(vec[x].s))){
                    get<1>(vec[x].s) = val;
                    get<2>(vec[x].s) = min(val,get<0>(vec[x].s));
                }
            }
        }
        get<0>(elem->second) > get<1>(elem->second) ? cout << "Case #" << i << ": " << get<0>(elem->second) << ' ' << get<1>(elem->second) << '\n' : cout << "Case #" << i << ": " << get<1>(elem->second) << ' ' << get<0>(elem->second) << '\n';
    }
}

