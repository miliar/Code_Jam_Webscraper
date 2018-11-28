#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int T;
long long N,K;
struct segment{
    int s,e,l,a;
    segment(){
        s = e = a = l = 0;
    }
    segment(int S,int E){
        s = S;
        e = E;
        a = (s+e)/2;
        l = e-s;
    }
    friend bool operator< (segment s1,segment s2){
        if( s1.l == s2.l)
            return s1.a > s2.a;//选最左
        return s1.l < s2.l;//长度按大到小
    }
}re;
ofstream fout("fout.txt");

void Solve(){
    priority_queue<segment> V;
    segment P(1,N);
    segment F;
    V.push(P);
    while(K--){
        F = V.top();
        V.pop();
        //cout<<F.s<<" "<<F.e<<" "<<F.a<<endl;
        if( F.a != F.s ){
            P = segment(F.s,F.a-1);
            V.push(P);
        }
        if( F.a != F.e ){
            P = segment(F.a+1,F.e);
            V.push(P);
        }

        if( K == 0 ){
            re = F;
        }
    }
}

int main(){
	int t;
	int j,l,r;

	cin>>T;
	for( j = 1; j<=T ; j++){
		cin>>N>>K;
		Solve();
            l = re.a - re.s;
		r = re.e - re.a;
		fout<<"Case #"<<j<<": ";
		if( l > r)
            fout<<l<<" "<<r<<endl;
        else
            fout<<r<<" "<<l<<endl;
	}
	return 0;
}
