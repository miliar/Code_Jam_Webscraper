                            #include <bits/stdc++.h>
                            #include<iostream>
                            #include<cstdio>
                            #include<vector>
                            #include<queue>
                            #include<map>
                            #include<cstring>
                            #include<string>
                            #include <math.h>
                            #include<algorithm>
                        //    #include <boost/multiprecision/cpp_int.hpp>
                            #include<functional>
                     #define int long long
                            #define inf  1000000007
                            #define pa pair<int,int>
                            #define ll long long
                            #define pal pair<double,int>
                            #define ppa pair<string,pa>
                            #define ssa pair<string,int>
                            #define  mp make_pair
                            #define  pb push_back
                            #define EPS (1e-10)
                            #define equals(a,b) (fabs((a)-(b))<EPS)
                     
                            using namespace std;
                     //priority_queue<int, vector<int>, greater<int> > que;
                            class Point{
                            	public:
                            	double x,y;
                            	Point(double x=0,double y=0):x(x),y(y) {}
                            	Point operator + (Point p) {return Point(x+p.x,y+p.y);}
                            	Point operator - (Point p) {return Point(x-p.x,y-p.y);}
                            	Point operator * (double a) {return Point(x*a,y*a);}
                            	Point operator / (double a) {return Point(x/a,y/a);}
                            	double absv() {return sqrt(norm());}
                            	double norm() {return x*x+y*y;}
                            	bool operator < (const Point &p) const{
                            		return x != p.x ? x<p.x: y<p.y;
                            	}
                            	bool operator == (const Point &p) const{
                            		return fabs(x-p.x)<EPS && fabs(y-p.y)<EPS;
                            	}
                            };
                            typedef Point Vector;
                     
                            struct Segment{
                            Point p1,p2;
                            };
                     
                        double hen(Vector a){
                        if(fabs(a.x)<EPS && a.y>0) return acos(0);
                        else if(fabs(a.x)<EPS && a.y<0) return 3*acos(0);
                        else if(fabs(a.y)<EPS && a.x<0) return 2*acos(0);
                        else if(fabs(a.y)<EPS && a.x>0) return 0.0;
                        else if(a.y>0) return acos(a.x/a.absv());
                        else return 2*acos(0)+acos(-a.x/a.absv());
                     
                        }
                     
                string itos( int i ) {
                ostringstream s ;
                s << i ;
                return s.str() ;
                }
                 
                int gcd(int v,int b){
                	if(v>b) return gcd(b,v);
                	if(v==b) return b;
                	if(b%v==0) return v;
                	return gcd(v,b%v);
                }
                            double dot(Vector a,Vector b){
                            	return a.x*b.x+a.y*b.y;
                            }
                            double cross(Vector a,Vector b){
                            	return a.x*b.y-a.y*b.x;
                            }
                        
                double distans(double x1,double y1,double x2,double y2){
                	double rr=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
                	return sqrt(rr);
                	
                }

                            //----------------kokomade tenpure------------


int T;
int a[2000],b[2000];
double pi=3.14159265358979323846264;

typedef pair<int,int> P;
struct edge{ int to,cap,cost,rev;};
vector<int> G[5010];
bool used[5010];
int match[5010];
int V;//VÇÕí∏ì_êî

void add_edge(int u,int v){
G[u].push_back(v);
G[v].push_back(u);
}

bool ddffss(int v){
used[v]=true;
  for(int i=0;i<G[v].size();i++){
    int u=G[v][i],w=match[u];
    if(w<0 || !used[w] &&ddffss(w)){
      match[v]=u;
      match[u]=v;
      return true;
    }
  }
  return false;
}

int bi_match(){
  int res=0;
  memset(match,-1,sizeof(match));
  for(int v=0;v<V;v++){
    if(match[v]<0){
      memset(used,0,sizeof(used));
      if(ddffss(v)){
        res++;
      }
    }
  }
  return res;
}
int n,k;
 signed  main(){
cin>>T;
 	
 	
 	
 	
 	for(int qwe=1;qwe<=T;qwe++){
 		for(int i=0;i<5000;i++){
 			G[i].clear();
 			used[i]=0;
 			match[i]=0;
 		}
 		for(int i=0;i<2000;i++){
 			a[i]=0;
 			b[i]=0;
 		}
 		int n,c,m,r,rr;
 		cin>>n>>c>>m;
 		int ak=0,bk=0,a1=0,b1=0;
 		
 		for(int i=0;i<m;i++){
 			cin>>r>>rr;
 			if(rr==1) {
 				ak ++;
 				a[ak-1]=r;
 				if(r==1) a1++;
 			}
 			else if(rr==2) {
 				bk ++;
 				b[bk-1]=r;
 				if(r==1) b1++;
 			}
 		}
 		int ans1,ans2;
 	//	cout<<a1<<" "<<b1<<endl;
 	//	cout<<ak<<" "<<bk<<endl;
 		if(a1==0 || b1==0) ans1=max(ak,bk);
 		else if(a1>=bk-b1) ans1=max(ak,bk+a1-(bk-b1));
 		else ans1=max(ak,a1+b1+(bk-b1)-a1);
 		
 		
 		if(ak<ans1){
 			for(int i=ak;i<ans1;i++) a[i]=0;
 		}
 		if(bk<ans1){
 			for(int i=bk;i<ak;i++) b[i]=0;
 		}
 		V=4400;
 		for(int i=0;i<ans1;i++){
 			for(int j=0;j<ans1;j++){
 				if(a[i]==b[j]) continue;
 				add_edge(i,2100+j);
 			}
 		}
 	//	cout<<ans1<<endl;
 		int y=bi_match();
 		ans2=ans1-y;
 	//	cout<<y<<endl;
 		cout<<"Case #"<<qwe<<": "<<ans1<<" "<<ans2<<endl;
 	
 	}
 //	cout<<i<<endl;
 	//  	printf("%.10f\n",ans[n-1]);
                    	return 0;
}