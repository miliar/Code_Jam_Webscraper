/*
 * This is my code,
 * my code is amazing...
 */
//Template v3.0 alfa 1 
#include <bits/stdc++.h>
#define ll long long
#define lld long double
#define pll pair<ll,ll>
#define pld pair<lld,lld>
#define vll vector<ll>
#define vvll vector<vll>
#define vpll vector<pll>
#define vvpll vector<vpll>
#define INF 1000000000000000047
const char en='\n';
#define prime 47
#define lprime 1000000000000000009
#define lldmin LDBL_MIN
#define MP make_pair
#define PB push_back
#define ff first
#define ss second
#define FOR(i,a,b) for(ll i=(ll)(a);i<=(ll)(b);i++)
#define FORD(i,a,b) for(ll i=(ll)(a);i>=(ll)(b);i--)
#define REP(i,b) for(ll i=0;i<(ll)(b);i++)
#define FORE(i,b) for(auto i=(b).begin(); i!=(b).end(); i++)
#define sqr(a) (a)*(a)
#define dst(a,b) sqr((a).ff-(b).ff)+sqr((a).ss-(b).ss)
#define mdst(a,b) abs((a).ff-(b).ff)+abs((a).ss-(b).ss)
//debug
#define debug 1
#define dbg(x) if(debug) cout<<#x<<"="<<(x)<<";"<<endl;
using namespace std;

template <class T, class U>
ostream& operator<<(ostream& out, const pair<T, U>&par) {
  out<<par.ff<<" "<<par.ss<<en;
  return out;
}
template <class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
  REP(i, v.size()){if(i) out<<" ";cout<<v[i];}
  return out;
}

struct
MaximumMatching {
vector< vector<
int
> > AB, BA;
MaximumMatching(
int
A,
int
B);
// parametre: velkosti particii
void
add_edge(
int
a,
int
b);
vector< pair<
int
,
int
> > maximum_matching();
pair< vector<
int
>, vector<
int
> > minimum_vertex_cover();
// {podmnozina vlavo,vpravo}
// maximum independent set == komplement minimum vertex coveru
};
MaximumMatching::MaximumMatching(
int
A,
int
B) { AB.resize(A); BA.resize(B); }
void
MaximumMatching::add_edge(
int
a,
int
b) { AB[a].push_back(b); BA[b].push_back(a); }
vector< pair<
int
,
int
> >
MaximumMatching::maximum_matching() {
int
A = AB.size(), B = BA.size();
vector<
int
> match(A,-1);
for
(
int
b=0; b<B; ++b) {
vector<
int
> from(A,-1);
queue<
int
> Q;
for
(
int
a : BA[b]) { Q.push(a); from[a]=a; }
while
(!Q.empty()) {
int
a = Q.front(); Q.pop();
if
(match[a] == -1) {
while
(from[a] != a) { match[a] = match[from[a]]; a = from[a]; }
match[a] = b;
break
;
}
else
{
for
(
int
x : BA[match[a]])
if
(from[x]==-1) { Q.push(x); from[x]=a; }
}
}
}
vector< pair<
int
,
int
> > result;
for
(
int
a=0; a<A; ++a)
if
(match[a] != -1) result.push_back( { a, match[a] } );
return
result;
}
pair< vector<
int
>, vector<
int
> >
MaximumMatching::minimum_vertex_cover() {
vector< pair<
int
,
int
> > matching = maximum_matching();
int
A = AB.size(), B = BA.size();
vector<
int
> match(A,-1);
vector<
bool
> matched(B,
false
), visited(A,
false
);
queue<
int
> Q;
for
(
auto
p : matching) { match[p.first]=p.second; matched[p.second]=
true
; }
for
(
int
b=0; b<B; ++b)
if
(!matched[b])
for
(
int
a : BA[b])
if
(!visited[a]) { visited[a]=
true
; Q.push(a); }
while
(!Q.empty()) {
int
a = Q.front(); Q.pop();
for
(
int
x : BA[match[a]])
if
(!visited[x]) { Q.push(x); visited[x]=
true
; }
}
vector<
int
> left_cover, right_cover;
for
(
int
a=0; a<A; ++a)
if
(visited[a]) left_cover.push_back(a);
else if
(match[a] != -1) right_cover.push_back( match[a] );
return
make_pair( left_cover, right_cover );
}




int main(){
	ios::sync_with_stdio(false);
        cin.tie(0);

	int T;
        cin>>T;
        FOR(t,1,T){
            cout<<"Case #"<<t<<": ";

            int n,c,mm;
            int pocet=0,prom=0;
            cin>>n>>c>>mm;

            vector<vector<ll>> V(3);
            REP(i,mm){
                int p,b;
                cin>>p>>b;
                //cout<<p<<" "<<b<<endl;
                V[b].PB(p);

            }

            sort(V[1].begin(),V[1].end());
            sort(V[2].begin(),V[2].end());
            
	    MaximumMatching m((int)V[1].size(),(int)V[2].size());
            REP(i,V[1].size())
                REP(j,V[2].size()){
                    if(V[1][i]!=V[2][j])
                        m.add_edge(i,j);
                }
            auto x=m.maximum_matching();
            multiset<int>M,N;

            REP(i,x.size()){
                M.insert(x[i].ff);
                N.insert(x[i].ss);
            }
            pocet+=x.size();

            vvll Z(3);
            
            REP(i,V[1].size()){
                if(M.find(i)==M.end())
                    Z[1].PB(V[1][i]);
                else
                    M.erase(M.find(i));
            }
            REP(i,V[2].size()){
                if(N.find(i)==N.end())
                    Z[2].PB(V[2][i]);
                else
                    N.erase(N.find(i));
            }
            
            if(Z[1].size()==0 || Z[2].size()==0){
                pocet+=max(Z[1].size(),Z[2].size());
            }
            else{
                if(Z[1][0]==1 && Z[2][0]==1){
                    pocet+=Z[1].size()+Z[2].size();
                }
                else{
                    pocet+=max(Z[1].size(),Z[2].size());
                    prom+=min(Z[1].size(),Z[2].size());
                }
            }


            cout<<pocet<<" "<<prom<<endl;
	}
}
