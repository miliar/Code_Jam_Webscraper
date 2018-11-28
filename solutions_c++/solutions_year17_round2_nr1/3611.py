#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <iostream>
#include <fstream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>
#include <thread>
#include <mutex>
#include <iomanip>

typedef long long i64;
typedef unsigned long long u64;
typedef unsigned int u32;
using namespace std;

typedef vector<int> VI;
#define endl '\n'

#define all(a) a.begin(),a.end()

const double pi = acos(-1.0);

int t;

struct Horse{
	double speed;
	double start;
};

int cmp(Horse a, Horse b) {
	return a.start > b.start;
}

int main() {
	ifstream in ("a.in");
	ofstream out ("a.out");
	
	out<<scientific;
	out<<scientific;
	out.precision(7);
	out.precision(7);
	
	
	in>>t;
	
	int testCase = 0;
	
	while(++testCase <= t) {
		double dest;
		int horsesLen;
		in>>dest>>horsesLen;
		vector<Horse> horses = vector<Horse>();
		while(--horsesLen >= 0) {
			double horseStart, horseSpeed;
			in>>horseStart>>horseSpeed;
			Horse currHorse;
			currHorse.start = horseStart;
			currHorse.speed = horseSpeed;
			horses.push_back(currHorse);
		}
		//out<<"sorting"<<endl;
		sort(horses.begin(), horses.end(), cmp);
		//out<<"sorted"<<endl;
		// Sortea bien

		int len = horses.size();

		//float meetingPoint = dest;
		double slowestTime = 0;

		for (int i = 0; i < len; i++) {
			double start = horses[i].start;
			double speed = horses[i].speed;
			
			double currTime = (dest-start) / speed;
			
			slowestTime = max(currTime, slowestTime);
		}
		
		double aveVelocity = dest/slowestTime;
		
		out<<"Case #"<<testCase<<": "<<aveVelocity<<endl;
		
		
		/*vector<double> meetingPoints = vector<double>();
		vector<double> timeToNext = vector<double>();
				
		// Must add first
		meetingPoints.push_back(0);
		timeToNext.push_back((dest-horses[len-1].start)/horses[len-1].speed);
		
		for(int i = len - 2; i >= 0; i--) {
			// si ves que es despues del meeting point,  probas con el siguiente caballo
		}
		meetingPoints.*/
		
		
		// Must reverse them later cause pushed in reverse order

	}
	

    return 0;
}
