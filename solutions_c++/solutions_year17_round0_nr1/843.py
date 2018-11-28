#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include <iomanip>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<set>
#include<bitset>
#include<map>
#include<queue>
#include<iterator>
#include<math.h>
#include <time.h>
using namespace std;
//set<int>::iterator it;
#define mdlo 1000000007
#define maxERR 0.00000001
//#define minVal -10000000000000
#define maxBits 40
#define pi 3.1415926535897932384626433832795
#define INF 999999999999
#define lim 10000007
typedef long long ll;
typedef vector<long>adjList;
typedef pair<long,long>edge;
typedef pair<ll,ll>ans;
long long mInv[200004];
long long fact[200004];
long long factInv[200004];
vector<edge>edges;
map<string,long>cityId;

adjList enemy[5];
map<vector<long>,long>dpmap;
vector<edge>criticalEdges;
adjList chlds[15];
adjList graph[200005];
ll heights[5];
ll segTree[5];
long nums[55];
long g[55];
long grid[15][15];
long base=1005;
vector<ll>primes;
vector<long>badPrimes;
long funcVal[1];
ll dfs_num[29],dfs_low[29],visited[2011],parent[1000123],criticalNode[19];
ll weightToparent[25];

long bff[1100];
long inq[1010];
long source;
ll N;
map<string,long>dict;
set<string>dictionary;
//set<string>::iterator it;
pair<set<string>::iterator,bool> ret;

typedef multiset<long> numset;
ll gcd(ll a,ll b){
    if(b==0)
        return a;
    if(a%b==0)
        return b;
    return gcd(b,a%b);
}
long long getmoduloInv(long long n){
    if(n==1)
        return 1;
    if(mInv[n]>0)
        return mInv[n];
    long long m=(-1*mdlo)/n;
    m+=mdlo;
    m*=getmoduloInv(mdlo%n);
    mInv[n]=(m%mdlo);
    return mInv[n];
}
bool rps(long r,long p,long s){
    long total=r+p+s;
    long maxv=max(r,max(p,s));
    long minv=min(r,min(p,s));
    long midv=total-(maxv+minv);
    if(maxv>minv+midv||(minv==0&&maxv>1))
        return false;
    if(maxv==2){
        if(minv==1)
            return true;
        return false;
    }
    long diffv=midv-minv;
    r=(maxv-diffv)/2;
    p=r+diffv;
    s=(total/2)-(r+p);
    return rps(r,p,s);
}
vector< ll> get_primes(unsigned long maxN){

    char *sieve;
    sieve = new char[maxN/8+1];
    // Fill sieve with 1
    long m=(maxN/8)+1;
    for(long long i=0;i<m;i++)
        sieve[i]=255;
    for(unsigned long x = 2; x <= maxN; x++)
        if(sieve[x/8] & (0x01 << (x % 8))){
            primes.push_back(x);
            // Is prime. Mark multiplicates.
            for(unsigned long j = 2*x; j <= maxN; j += x)
                sieve[j/8] &= ~(0x01 << (j % 8));
        }
    delete[] sieve;
    return primes;
}
ll getPow(ll b,ll p){
  if(b<2||p==1)
    return b;
  if(p==0)
    return 1;
  ll val=getPow(b,p/2);
  val*=val;
 // val%=mdlo;
  if(p%2==1){
    val*=b;
 //   val%=mdlo;
  }
  return val;
}

long long sumPoles[8];
long long diffPoles[8];
void buildDiffSegTree(long node,long b,long e){
    if(b==e)
        segTree[node]=b;
    else{
        long mid=(b+e)/2;
        buildDiffSegTree(node*2,b,mid);
        buildDiffSegTree(1+node*2,mid+1,e);
        if(diffPoles[segTree[node*2]]<diffPoles[segTree[1+node*2]])
            segTree[node]=segTree[1+node*2];
        else
            segTree[node]=segTree[node*2];
    }
}
void buildSumSegTree(long node,long b,long e){
    if(b==e)
        segTree[node]=b;
    else{
        long mid=(b+e)/2;
        buildSumSegTree(node*2,b,mid);
        buildSumSegTree(1+node*2,mid+1,e);
        if(sumPoles[segTree[node*2]]<sumPoles[segTree[1+node*2]])
            segTree[node]=segTree[1+node*2];
        else
            segTree[node]=segTree[node*2];
    }
}
long long getMaxDiff(long node,long segBeg,long segEnd,long qBeg,long qEnd){
    if(segEnd<qBeg||segBeg>qEnd)
        return N+1;
    if(segBeg>=qBeg&&segEnd<=qEnd)
        return segTree[node];
    long mid=(segBeg+segEnd)/2;
    long fh=getMaxDiff(node*2,segBeg,mid,qBeg,qEnd);
    long sh=getMaxDiff(1+node*2,mid+1,segEnd,qBeg,qEnd);
    if(fh==N+1)
        return sh;
    if(sh==N+1)
        return fh;
    if(diffPoles[sh]<diffPoles[fh])
        return fh;
    return sh;
}
long long getMaxSum(long node,long segBeg,long segEnd,long qBeg,long qEnd){
    if(segEnd<qBeg||segBeg>qEnd)
        return N+1;
    if(segBeg>=qBeg&&segEnd<=qEnd)
        return segTree[node];
    long mid=(segBeg+segEnd)/2;
    long fh=getMaxSum(node*2,segBeg,mid,qBeg,qEnd);
    long sh=getMaxSum(1+node*2,mid+1,segEnd,qBeg,qEnd);
    if(fh==N+1)
        return sh;
    if(sh==N+1)
        return fh;
    if(sumPoles[sh]<sumPoles[fh])
        return fh;
    return sh;
}
long dfs(long node,long curLen){
    if(inq[node]==0){
        inq[node]=1;
        dfs(bff[node],curLen+1);
    }
  return 0;
}
//long dp[129][129][129];
map<ll,ll>divPos;
long col[25];
void bfs(ll node){
    col[node]=2;
    for(long i=0;i<graph[node].size();i++){
        if(col[graph[node][i]]!=2)
            bfs(graph[node][i]);
    }
}
long getParent(long node){
    if(node!=parent[node]){
        parent[node]=getParent(parent[node]);
    }
    return parent[node];
}
void unionNode(long nodeA,long nodeB){
    long parentA=getParent(nodeA);
    long parentB=getParent(nodeB);
    if(parentA<parentB)
        parent[parentB]=parentA;
    else
        parent[parentA]=parentB;
}
bool isSmallPrime(ll n){
    long low=0,high=primes.size()-1,mid;
    mid=(low+high)/2;
    while(low<=high){
        if(primes[mid]==n)
            return true;
        if(primes[mid]>n)
            high=mid-1;
        else
            low=mid+1;
        mid=(low+high)/2;
    }
    return false;
}
bool isprimeNum(ll n){
    long pos=0;
    ll limt=1+(sqrt((double)n));
    if(n<=primes[primes.size()-1])
        return isSmallPrime(n);
    while(pos<primes.size()&&primes[pos]<limt){
        if(n%primes[pos]==0)
            return false;
        pos++;
    }
    return true;
}
void createDummyTestCases(){
freopen ("E:/outputSmall.txt","w",stdout);
    srand (time(NULL));
    string dt="DR";
    for(long i=0;i<200000;i++){
        cout<<dt[rand()%2];
    }
}
typedef pair<long,long>dpStart;
long long vals[1];
void buildMaxSegTree(long node,long startPos,long endPos){
    if(startPos==endPos){
        segTree[node]=startPos;
        return;
    }
    else{
        long midPos=(startPos+endPos)/2;
        buildMaxSegTree(node*2,startPos,midPos);
        buildMaxSegTree(1+(2*node),midPos+1,endPos);
        if(vals[segTree[2*node]]>vals[segTree[1+(2*node)]])
            segTree[node]=segTree[2*node];
        else
            segTree[node]=segTree[1+(2*node)];
    }
}
long long getMaxFromSegTree(long node,long segBeg,long segEnd,long qStart,long qEnd){
    if(qStart>segEnd||qEnd<segBeg)
        return -1;
    if(segBeg>=qStart&&segEnd<=qEnd)
        return segTree[node];
    long segMid=(segBeg+segEnd)/2;
    long long fh=getMaxFromSegTree(node*2,segBeg,segMid,qStart,qEnd);
    long long sh=getMaxFromSegTree(1+(node*2),segMid+1,segEnd,qStart,qEnd);
    if(fh<0)
        return sh;
    if(sh<0)
        return fh;
    if(vals[sh]<vals[fh])
        return fh;
    return sh;
}
long element[1];

typedef vector<ll>megprime;
megprime megaprimes[20];
bool isPrime(string s){
    ll v=0;
    for(ll i=0;i<s.size();i++){
        v=(v*(ll)10)+(ll)+(ll)(s[i]-'0');
    }
    return isprimeNum(v);
}

bool isPrimeDigit(long n){
    if(n==2||n==3||n==5||n==7)
        return true;
    return false;
}

long perm[25];
vector<long>seq;
void eulerTour(long node){
    seq.push_back(node);
    visited[node]=1;
    for(long i=0;i<graph[node].size();i++){
        if(visited[graph[node][i]]==0){
            eulerTour(graph[node][i]);
            seq.push_back(node);
        }
    }
}
ll dp[2][7070];
ll moves[2][7070];
ll k[2];
ll n,K;
queue<long>flips;
char curFace;
long flipCount;
void flip(){
    if(curFace=='+')
        curFace='-';
    else
        curFace='+';
}
bool startFlip(long pos){
    if(pos+K>n)
        return false;
    flip();
    flipCount++;
    flips.push(pos);
    return true;
}
void endFlip(){
    flip();
    flips.pop();
}
int main(void){
    freopen ("E:/inputSmall.txt","r",stdin);

    freopen ("E:/outputSmall.txt","w",stdout);
    ll test_cases=1,seed=1,f,ans=0,g;
  cout << setprecision(15) << fixed;
  //createDummyTestCase();
    cin>>test_cases;
    string s1,s2[1010];
    //printV();
    long long m,a,b,c=0,q,l,d;

    for(long T=0;T<test_cases;T++){
        cin>>s1;
        cin>>K;
        while(!flips.empty())
            flips.pop();
        flipCount=0;
        curFace='+';
        n=s1.size();
        bool possible=true;
        for(long i=0;i<n;i++){
            if(!flips.empty()&&flips.front()+K==i){
                endFlip();
            }
            if(s1[i]!=curFace){
                if(!startFlip(i)){
                    possible=false;
                    break;
                }
            }
        }
        printf("Case #%ld: ",T+1);
        if(possible)
            cout<<flipCount<<endl;
        else
            cout<<"IMPOSSIBLE\n";
    //fill(dp[0][0], dp[0][0]+205*105*105, -1.0);


        //check();
    }
    return 0;
}
