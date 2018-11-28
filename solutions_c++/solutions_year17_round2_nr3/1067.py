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
int uu,vv;
int n,q;
int a[101][101];
int e[101],s[101];
double dp[101][101];
int dist[101];
int dist2[101][101];
bool sumi[101][101]={0};



double saiki(int g,int st){
	if(sumi[st][g]==1) return dp[st][g];
	
	
	double w=10000000000000.0;
	if(dist2[st][g]<=e[st]) w=(dist2[st][g]+0.0)/(s[st]+0.0);
//	cout<<w<<endl;
	for(int i=st+1;i<g;i++){
		w=min(w,saiki(i,st)+saiki(g,i));
	}
	sumi[st][g]=1;
	dp[st][g]=w;
	
//	cout<<st<<" "<<g<<" "<<w<<endl;
	return w;
	
}

 signed  main(){
cin>>T;
 	
 	
 	
 	
 	for(int qwe=1;qwe<=T;qwe++){
 		
 		for(int i=0;i<n;i++){
 			e[i]=0;
 			s[i]=0;
 			dist[i]=0;
 			for(int j=0;j<n;j++){
 				a[i][j]=0;
 				dist2[i][j]=0;
 				dp[i][j]=0;
 				sumi[i][j]=0;
 			}
 		}
 		
 		
 		cin>>n>>q;
 		for(int i=0;i<n;i++){
 			cin>>e[i]>>s[i];
 		}
 		for(int i=0;i<n;i++)for(int j=0;j<n;j++)cin>> a[i][j];
 		cin>>uu>>vv;
 		for(int i=0;i<n-1;i++) dist[i]=a[i][i+1];
 	//	cout<<dist[0]<<endl;
 		for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
 			int er=0;
 			for(int k=i;k<j;k++) er+= dist[k];
 			dist2[i][j]=er;
 		//	cout<<er<<endl;
 		}
 		
 		
 		
 		
 		
 		cout<<"Case #"<<qwe<<": ";
 		printf("%.10f\n",saiki(n-1,0));
 	}
 //	cout<<i<<endl;
 //	  	printf("%.10f\n",saiki(n-1,0));
                    	return 0;
}