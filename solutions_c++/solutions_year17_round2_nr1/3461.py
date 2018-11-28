#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <cstdio>
using namespace std;

long double maxSpeed(unsigned long long int d,
                   vector<unsigned long long int>& horse,
                   vector<unsigned long long int>& speed ){
    long double x = 0, t;
    for(unsigned long long int i=0; i < horse.size(); ++ i){
        t = (d-horse[i])*1.0/speed[i];
        if(  t > x) x = t;
    }
    return d*1.0/x;
}


int main()
{

    freopen("d://A-large.in", "r", stdin);
    freopen("d://A-large.out", "w", stdout);

	int numcase;
	cin >> numcase;
	cout<<setiosflags(ios::fixed);
	cout<<setprecision(6);
	for(int i=0; i<numcase; i++) {
        unsigned long long int d, horseNum, pos, s;
        vector<unsigned long long> horse, speed;
        cin>>d>>horseNum;
        for(unsigned long long int i = 0; i < horseNum; i++){
            cin>>pos>>s;
            horse.push_back(pos);
            speed.push_back(s);
        }
        cout << "case #" << (i+1) << ": " << maxSpeed(d, horse, speed) << endl;
	}
	return 0;
}
