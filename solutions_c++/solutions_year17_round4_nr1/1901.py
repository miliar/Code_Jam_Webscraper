#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define ft first
#define sc second

#define eps 1e-11
#define PI acos(1.0)

typedef long int li;
typedef long long int lli;
typedef unsigned long long int ull;

using namespace std;
const int MAX = 1e3+5;
const ull mod = 1e9+7;

// Fast Input -------------------------------------------------------------------------------------------------

/*
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x)

template<typename T>
void inpos(T &x){
    x=0;
    register T c=gc();
    while(((c<48)||(c>57))&&(c!='-'))
        c=gc();
    bool neg=false;
    if(c=='-')
        neg=true;
    for(;c<48||c>57;c=gc());
    for(;c>47&&c<58;c=gc())
        x=(x<<3)+(x<<1)+(c&15);
    if(neg)x=-x;
}

template<typename T>
void outpos(T n){
    if(n<0){
        pc('-');
        n*=-1;
    }
    char snum[65];
    int i=0;
    do {
        snum[i++]=n%10+'0';
        n/=10;
    }while(n);
    i=i-1;
    while(i>=0)
        pc(snum[i--]);
    pc('\n');
}*/

// Number Theory stuff -------------------------------------------------------------------------------------------

template<typename T>
T pow (T a, T b){
    T x=1, y=a;
    while(b){
        if(b&1){
            x = (x*y);
            if(x>mod)
                x%=mod;
        }
        y*=y;
        if(y>mod)
            y%=mod;
        b>>=1;
    }
    return x;
}

template<typename T>
T modInverse(T a){
    return pow(a,mod-2);
}

template<typename T>
T nCr(T N, T r){
    if(N-r>r)
        r = N-r;
    T num = (T)1;
    for(T i=N; i>r; i--){
        num = (num*i)%mod;
    }
    T denom = (T)1;
    for(T i=1; i<=(N-r); i++){
        denom = (denom*i)%mod;
    }
    return (T)(num * modInverse(denom))%mod;
}

template<typename T>
T etf(T N){
    T ans = N, root;
    root = (T)sqrt(N);
    for(T i=2; i<=N; i++){
        if(i>root)
            break;
        if(!(N%i)){
            ans -= (T)(ans/i);
        }
        while(N%i == 0){
            N /= i;
        }
    }
    if(N>1)
        ans -= ans/N;
    return ans;
}

// Data-Structure stuff --------------------------------------------------------------------------------

struct heapCmp{
    bool operator()(int i, int j){
        return i>j;
    }
};

//priority_queue<int, vector<int>, heapCmp> minHeap;
//priority_queue<int, vector<int> > maxHeap;

template<typename T>
bool cmp(T x, T y){
    return x > y;   //returns true if x>y(reversed the order)
}

// For Ease-of-Use --------------------------------------------------------------------------------------

template<typename T>
ostream& operator<< (ostream &o, vector<T> V){
    o<<"Size = "<<V.size()<<"\n";
    if(V.size()==0)
        return o;
    for(int i=0;i<V.size();i++){
        o << V[i] << " ";
    }
    return o<<endl;
}

template<typename T>
ostream& operator<< (ostream &o, vector<vector<T> > V){
    o<<"N = "<<V.size();
    if(V.size())
        o<<"\tM = "<<V[0].size()<<"\n";
    else{
        o<<"\tM = 0\n";
    }
    for(int i=0;i<V.size();i++){
        for(int j=0;j<V[0].size();j++){
            o<<V[i][j]<<" ";
        }
        cout<<"\n";
    }
    return o;
}

template<typename U,typename V>
ostream& operator<< (ostream &o, pair<U,V> p){
    return o<<"("<<p.first<<", "<<p.second<<") ";
}

template<typename T>
istream& operator>> (istream &in, vector<T> &v){
    for(unsigned i=0; i<v.size(); i++)
        in>>v[i];
    return in;
}

// Solution starts here ------------------------------------------------------------------------

int rem[MAX];
int remCnt[MAX];
int G[MAX];

int main(){
    freopen("A-small-attempt3.in", "r", stdin);
    freopen("A-small-attempt3.out", "w", stdout);

    int T,N,P;
    cin>>T;
    for(int z=1;z<=T;z++){
        cin>>N>>P;
        //cout << N << " "  << P << "\n";
        memset(rem,0,sizeof(rem));

        for(int i=0;i<N;i++){
            cin>>G[i];
            //cout << G[i] << " ";
            rem[G[i]%P] += 1;
            remCnt[G[i]%P] += 1;
        }
        //cout << "\n";

        /*cout << "\nrem: ";
        for(int i=0;i<P;i++){
            cout << rem[i] << " ";
        }
        cout << "\n";*/

        int ans=0;
        for(int i=0;i<P;i++){
            if(i==0){
                ans+=rem[i];
                rem[i] = 0;
            }
            else{

                    int tmp = min(rem[i],rem[P-i]);
                    if(i!=P-i)
                        ans += tmp;
                    else
                        tmp = 0;
                    //cout << "i = " << i << "\ttmp= "<<tmp<<"\n";
                    if(tmp<rem[i]){
                        int cnt = (rem[i]-tmp)*i;
                        int lcm = (P*i)/__gcd(P,i);
                        /*int base = 0;
                        while(base<P){
                            base += i;
                        }*/

                        ans += (int)(cnt/lcm) + 1;
                        if(cnt%lcm==0)
                            ans-=1;
                    }
                    rem[i] = 0; rem[P-i] -= tmp;

            }
        }
        cout << "Case #"<< z << ": " << ans << "\n";
    }

    return 0;
}
