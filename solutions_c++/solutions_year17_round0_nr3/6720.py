#include <bits/stdc++.h>
using namespace std;

#define inf                         INFINITY
#define bitcount                    __builtin_popcount  // counts 1 eg- 1101 has value 3

/*
   const clock_t begin_time = clock();
   // do something
   cout << float( clock () - begin_time ) /  CLOCKS_PER_SEC << endl;

   Read from a file
   freopen("input.in","r",stdin);
   freopen("output.out","w",stdout);
 */

#define TRACE
#ifdef TRACE
template<class T>
ostream& operator<<(ostream& out, const tuple<T>& a) {
        out << "[" << get<0>(a) << "]"; return out;
}
template<class T, class U>
ostream& operator<<(ostream& out, const tuple<T, U>& a) {
        out << "[" << get<0>(a) << " " << get<1>(a) << "]"; return out;
}
template<class T, class U, class V>
ostream& operator<<(ostream& out, const tuple<T, U, V>& a) {
        out << "[" << get<0>(a) << " " << get<1>(a) << " " << get<2>(a) << "]"; return out;
}
template<class T, class U, class V, class W>
ostream& operator<<(ostream& out, const tuple<T, U, V, W>& a) {
        out << "[" << get<0>(a) << " " << get<1>(a) << " " << get<2>(a) << " " << get<3>(a) << "]"; return out;
}
template<class T, class U>
ostream& operator<<(ostream& out, const pair<T, U>& a) {
        out << "[" << a.first << " " << a.second << "]"; return out;
}
template<class T>
ostream& operator<<(ostream& out, const vector<T>& a) {
        out << "[ "; for (auto &it : a) out << it << " "; out << "]"; return out;
}
template<class T>
ostream& operator<<(ostream& out, const set<T>& a) {
        out << "[ "; for (auto &it : a) out << it << " "; out << "]"; return out;
}
template<class T>
ostream& operator<<(ostream& out, const multiset<T>& a) {
        out << "[ "; for (auto &it : a) out << it << " "; out << "]"; return out;
}
template<class T, class U>
ostream& operator<<(ostream& out, const map<T, U>& a) {
        for (auto &it : a) out << it.first << " -> " << it.second << " | "; return out;
}
template<class T, class U>
ostream& operator<<(ostream& out, const multimap<T, U>& a) {
        for (auto &it : a) out << it.first << " -> " << it.second << " | "; return out;
}
#define pra(a,n) cerr<<# a<<" : "; for(int i=0; i<n; ++i) cerr<<a[i]<<" "; cerr<<endl;
#define praa(a,n,m) cerr<<# a<<" : "<<endl; for(int i=0; i<n; ++i) {for(int j=0; j<m; ++j) cerr<<a[i][j]<<" "; cerr<<endl; }
#define trace(...) __f(# __VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
        cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename ... Args>
void __f(const char* names, Arg1&& arg1, Args&& ... args) {
        const char* comma = strchr(names + 1, ','); cerr.write(names, comma - names) << " : " << arg1 << " | "; __f(comma + 1, args ...);
}
#else
#define trace(...)
#define pra(a,n)
#define praa(a,n,m)
#endif

void r(){
};
template<typename T,typename ... Args>
void r(T &a, Args& ... args) {
        cin>>a; r(args ...);
}

void p(){
        cout <<"\n";
};
template<typename T,typename ... Args>
void p(T &a, Args& ... args) {
        cout << a << " "; p(args ...);
}

template<class T> T gcd(T a, T b) {
        return a ? gcd (b % a, a) : b;
}
template<class T> T lcm(T a, T b) {
        return  ((a*b)/gcd (b % a, a));
}

/*
   template<class T1> T1 binpow_template(T1 x, T1 n)
   {
        if (n==0) return 1;
        ll temp=bigMod(x, n/2);
        return n%2==0 ? (temp*temp) : (x*((temp*temp)));
   }
 */

long long mod;
long long  bigMod( long long x,  long long n)
{
        if (n==0) return 1;
        long long temp=bigMod(x, n/2);
        return n%2==0 ? (temp*temp)%mod : (x*((temp*temp)%mod))%mod;
}

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)

#define fa(i, begin, end)           for (auto i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define fe(v, c)                    for(auto v : c)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ((b).find(a) != (b).end())
#define pb                          emplace_back  // this will work almost always
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((auto)(a.size()))
#define mt                          make_tuple
#define mp                          make_pair

#define checkbit(n,b)               ((n >> b) & 1)
#define DREP(a)                     sort(all(a)); a.erase(unique(all(a)),a.end()) //deletes repeat
#define sqr(x)                      ((x) * (x))
#define sqrt(x)                     sqrt(abs(x))

#define bit(x,i)                    (x&(1<<i))  //select the bit of position i of x
#define lowbit(x)                   ((x)&((x)^((x)-1))) //get the lowest bit of x
#define higbit(x)                   (1 << (auto) log2(x) )

#define ft                          first
#define sd                          second
#define pq                          priority_queue

#define ll long long
#define st string
#define ld long double

int slate[1120];

pair<int, int > fille(int lim){
        int lef[1013], rig[1123];
        fa(i,1,lim) if(slate[i] == 0) lef[i] = lef[i-1]+1;
        else lef[i] = 0;
        for(int i = lim; i>0; i--) if(slate[i] == 0) rig[i] = rig[i+1]+1;
                else rig[i] = 0;
        pair<int, int >bedd, tedd;
        fa(i,0,lim){
                if(min(lef[i],rig[i])>bedd.ft and slate[i]!=1 ) {
                        bedd.ft = min(lef[i],rig[i]);
                        bedd.sd = i;
                }
        }
        fa(i,0,lim){
                if(max(lef[i],rig[i])>tedd.ft and min(lef[i],rig[i]) == bedd.ft and slate[i]!=1) {
                        tedd.ft = max(lef[i],rig[i]);
                        tedd.sd = i;
                }
        }
        int multa = 0;
        fa(i,0,lim) if(min(lef[i],rig[i]) == bedd.ft) multa++;
        //   trace(bedd,tedd,multa);
        if(multa>1) slate[tedd.sd] = 1;
        else slate[bedd.sd] = 1;
        //  fa(i,0,lim ) cout << slate[i];
        return mp(tedd.ft,bedd.ft);
}



int main()
{
        boost;
        int n, k,test;
        freopen("input.in","r",stdin);
        freopen("output.out","w",stdout);
        r(test);
        fa(i,0,test){
                r(n, k);
                fa(i,0,n+2) slate[i]= 0;
                slate[0]= 1;
                slate[n+1] = 1;
                pair<int,int > ans;
                fa(i,0,k) ans = fille(n+2);
                cout << "Case #" << i+ 1<< ": " << ans.ft-1 << " " << ans.sd-1 << "\n";
        }
}

/*
   Sample Tests
   1->  input

        output

   2->  input

        output

   3->  input

        output

 */
