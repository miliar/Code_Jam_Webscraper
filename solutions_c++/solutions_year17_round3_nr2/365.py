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
vector<pa> a;

 signed  main(){
cin>>T;
 	
 	
 	
 	
 	for(int qwe=1;qwe<=T;qwe++){
 		a.clear();
 	//	cout<<"   "<<endl;
 		int z[3000]={0};
 		int ac,aj;
 		cin>>ac>>aj;
 		int jikan=0;;
 		for(int i=0;i<ac;i++){
 			int er,err;
 			cin>>er>>err;
 			jikan += err-er;
 			a.pb(mp(er,err));
 			for(int j=er;j<err;j++) {
 				z[j]=1;
 				z[j+1440]=1;
 			}
 		}
 		int ans=ac;
 		sort(a.begin(),a.end());
 		for(int i=0;i<ac-1;i++) if(a[i].second==a[i+1].first)ans--;
 		
 		if(z[0]==1 && z[1439]==1) ans--;
 		
 		for(int i=0;i<aj;i++){
 			int er,err;
 			cin>>er>>err;
 		//	jikan += err-er;
 			
 			for(int j=er;j<err;j++) {
 				z[j]=2;
 				z[j+1440]=2;
 			}
 		}
 		int l;
 		for(int i=0;i<3000;i++){
 			if(z[i]!=0){
 				l=i;
 				break;
 			}
 		}
 		priority_queue<int, vector<int>, greater<int> > aa,ab;
 		priority_queue<int > bb;
 		int abh=0;
 		for(int i=l;i<=1440+l;i++){
 			if(z[i]!=0) continue;
 			int hi,mi,miz,hiz=i;
 			hi=z[i-1];
 			int it=i;
 			while(z[it]==0) it++;
 			mi=z[it];
 			miz=it;
 			i=it-1;
 		//	cout<<hi+mi<<" "<<miz-hiz<<endl<<endl;
 			if(hi+mi==2) aa.push(miz-hiz);
 			if(hi+mi==3){
 				ab.push(miz-hiz);
 				abh += miz-hiz;
 			}
 			if(hi+mi==4) bb.push(miz-hiz);
 		}
 //		cout<<"jikan "<<jikan<<endl;
 //		cout<<ans<<endl;
 		while(aa.size()>0){
 			int ed=aa.top();
 			if(jikan+ed<=720){
 				aa.pop();
 				ans--;
 				jikan +=ed; 
 			}
 			else {
 				jikan=720;
 				break;
 			}
 		}
 //	cout<<"jikan "<<jikan<<" "<<ans<<endl;
 		if(jikan+abh>=720) jikan=720;
 		else jikan += abh;
 		
 //		cout<<"jikan "<<jikan<<" "<<ans<<endl;
 		while(jikan <720){
 			int r=bb.top();
 			bb.pop();
 			ans++;
 			jikan += r;
 		}
 		cout<<"Case #"<<qwe<<": "<<2*ans<<endl;;
 	//	printf("%.10f\n",me);
 	}
 //	cout<<i<<endl;
 	//  	printf("%.10f\n",ans[n-1]);
                    	return 0;
}