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
    cout<<1000<<endl;
    for(long i=100;i<=100000;i+=100){
        cout<<"100000 "<<i<<endl;
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

long queens[110];
long colTaken[110];
long diagnoalsumOccupied[210];
long diagnoaldiffOccupied[210];
void placeQueen(long row,long col){
    long sum=row+col;
    long diff=110+row-col;
    diagnoaldiffOccupied[diff]=1;
    diagnoalsumOccupied[sum]=1;
    queens[row]=col;
    colTaken[col]=1;
}
void unplaceQueen(long row){
    long col=queens[row];
    long sum=row+col;
    long diff=110+row-col;
    diagnoaldiffOccupied[diff]=0;
    diagnoalsumOccupied[sum]=0;
    queens[row]=0;
    colTaken[col]=0;
}
bool backTrackPlaceQueen(long pos){
    for(long i=1;i<=N;i++){
        long sum=pos+i;
        long dif=110+pos-i;
        if(diagnoaldiffOccupied[dif]==0&&diagnoalsumOccupied[sum]==0&&colTaken[i]==0){
            placeQueen(pos,i);
            if(pos==N){
                unplaceQueen(pos);
                return true;
            }
            if(backTrackPlaceQueen(pos+1)){
                unplaceQueen(pos);
                return true;
            }
            unplaceQueen(pos);

        }
    }
}
void printFirstSolution(long N){
    memset(queens,0,sizeof(queens));
    memset(diagnoaldiffOccupied,0,sizeof(diagnoaldiffOccupied));
    memset(diagnoalsumOccupied,0,sizeof(diagnoalsumOccupied));
    memset(colTaken,0,sizeof(colTaken));
    if(backTrackPlaceQueen(1)){
        for(long i=0;i<N;i++)
            cout<<queens[i+1]<<" ";
    }

}
vector<long> getDigits(string s){
    vector<long> digits;
    for(long i=0;i<s.size();i++)
        digits.push_back(s[i]-'0');
    return digits;
}

ll getStringVal(string s){
    ll val=0;
    for(long i=0;i<s.size();i++)
        val=val*10+(s[i]-'0');
    return val;
}

bool matchString(string s1,string s2){
    for(long i=0;i<s1.size();i++){
        if(s1[i]!=s2[i]&&s1[i]!='?'&&s2[i]!='?')
            return false;
    }
    return true;
}

unsigned int fact2(int x){
  return(x*fact2(x-1));
}
ll elementCount[65600];
typedef vector<long> combinatinIds;
combinatinIds allCombinations[20];
ll getElementCount(ll combNum){
    if(elementCount[combNum]==-1){
        ll temp=combNum;
        if(temp==0)
            elementCount[combNum]=0;
        else{
            elementCount[combNum]=(temp%2)+getElementCount(temp/2);
        }
    }
}
void buildCombinations(ll N){
    ll totalComb=1;
    totalComb=totalComb<<N;
    memset(elementCount,-1,sizeof(elementCount));
    elementCount[0]=0;
    for(long i=1;i<totalComb;i++){
        elementCount[i]=elementCount[i/2]+(i%2);
        allCombinations[elementCount[i]].push_back(i);
    }
}
typedef pair<ll,ll> pancake;
pancake pancakes[1100];
ll dp[1100][1100];
ll getArea(ll pos,ll rem){
    if(dp[pos][rem]==-1){
        if(pos+rem>N||rem==0)
            return 0;
        dp[pos][rem]=2*pancakes[pos].first*pancakes[pos].second+getArea(pos+1,rem-1);
        if(getArea(pos+1,rem)>dp[pos][rem])
            dp[pos][rem]=dp[pos+1][rem];
    }
    return dp[pos][rem];
}
int main(void){
    freopen ("E:/inputSmall.txt","r",stdin);
//createDummyTestCases();
    freopen ("E:/outputSmall3.txt","w",stdout);
    ll test_cases=1,seed=1,f,ans=0;
  cout << setprecision(15) << fixed;
  //createDummyTestCase();
    cin>>test_cases;
    string s,s1;
    buildCombinations(16);
    ll R,C,Ten;
    for(long T=0;T<test_cases;T++){

           //fill(dp[0][0], dp[0][0]+205*105*105, -1.0);
        //cin>>healthDragon>>attack>>knightHealth>>attackKnight>>buff>>debuff;
        cout<<"Case #"<<T+1<<": ";
        memset(dp,-1,sizeof(dp));
        memset(pancakes,0,sizeof(pancakes));
        double D,S,K,Si,t=0,tMax=0;

        cin>>N>>K;
        for(long i=0;i<N;i++){
            cin>>pancakes[i].first>>pancakes[i].second;
        }
        sort(pancakes,pancakes+N);
        reverse(pancakes,pancakes+N);

        ll maxArea=0;
        for(long i=0;i<N;i++){
            ll area=pancakes[i].first*pancakes[i].first+2*pancakes[i].first*pancakes[i].second;
            ll nextArea=0;
            for(long j=i+1;j<N;j++){
                if(getArea(j,K-1)>nextArea)
                    nextArea=getArea(j,K-1);
            }
            area+=nextArea;
            if(area>maxArea)
                maxArea=area;
        }
        double area=maxArea;
        area*=pi;
        cout<<area;
        cout<<endl;

    }
    return 0;
}

