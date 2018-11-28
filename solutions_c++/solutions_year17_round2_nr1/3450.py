#include <iostream>
#include <fstream>
#include <ostream>
#include <vector>
#include <sstream>
#include <unordered_set>
#include <limits>
#include <iomanip>

using namespace std;


typedef std::numeric_limits< double > dbl;
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

typedef vector<vector<char>> vv;
int postion(int a, int b, int m){
    return a*m+b;
}

typedef const int& CI;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)


typedef long long int ll;
typedef vector<pair<int,int>> vp;

float maxspeed(vp& p, int d){
    float max_time=-1;
    for(auto& pa:p){
        float r=d-pa.first;
        float time=(float)r/ (double)pa.second;
        if(max_time<time) max_time=time;
    }
    float res=d/max_time;
    //cout<<max_time<<endl;
    return res;
}

int main(){
    ifstream f("small.txt");
    ofstream myfile("output.txt");
    int N;
    f>>N;
    rep2(nn,1,N+1) {
        string str;
        int D,N1,K,S;
        f>>D>>N1;
        vp p;
        for(int j=0;j<N1;j++){
            f>>K>>S;
            p.push_back(make_pair(K,S));
        }
        float res=maxspeed(p, D);
        //cout<<res<<" case"<<nn<<endl;
//        std::cout << std::fixed;
//        std::cout << std::setprecision(6);
        myfile << "Case #"<<nn<<": "<<std::fixed<<std::setprecision(6)<<res<<endl;
    }
    myfile.close();
    
    return 0;
}




