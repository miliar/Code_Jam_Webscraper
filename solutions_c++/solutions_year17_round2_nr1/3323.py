#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

int main() {
	int T,cases = 1;
	cin>>T;
	for (cases = 1; cases <= T;cases++) {
        int dist,N;
        cin>>dist>>N;
        double slowest = -1.0;
        for ( int i = 0; i<N; i++) {
            int pos,speed;
            cin>>pos>>speed;
            double time;
            time = (dist-pos)/(speed*1.0);
            if ( time >slowest)
                slowest = time;
        }
        cout<<fixed;
        cout<<setprecision(6);
        cout<<"Case #"<<cases<<": "<<(dist/(slowest*1.0))<<endl;
	}
	return 0;
}
