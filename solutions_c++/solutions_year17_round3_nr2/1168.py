#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
//############################################################################
//#include <rapidcheck.h>
// rc::check("Test", [](){ const auto i = *rc::gen::inRange(0, 10); return i < 10 && i >= 0; });
// https://github.com/emil-e/rapidcheck/
//#include <boost/multiprecision/cpp_int.hpp> //MULTIPRECISION
//#include <boost/foreach.hpp> //BOOST_FOREACH( single, sequence ) {}
//###########################################################################
//
using Owner = enum{c, j};
struct Task{
	Owner o;
	int start, end;
};

string process(vector<Task>& v){
	int swaps = 0;
	int tC = 720, tJ = 720;
	for(Task t : v){
		if(t.o == c) tC -= (t.end - t.start);
		else tJ -= (t.end - t.start);
	}
	sort(v.begin(), v.end(), [](const Task& a, const Task& b){ return a.start < b.start; });
	v.push_back(v[0]);
	v.back().start += 1440;
	v.back().end += 1440;
	for(int i = 1 ; i < v.size() ; ++i){
		if(v[i].o != v[i - 1].o)
			swaps++;
		else{
			if(v[i].o == c){
			if(v[i].start - v[i-1].end <= tC) tC -= v[i].start - v[i-1].end;
			else {swaps += 2;}
			}
			if(v[i].o == j){
			if(v[i].start - v[i-1].end <= tJ) tJ -= v[i].start - v[i-1].end;
			else {swaps += 2;}
			}
		}
	}

	return to_string(swaps);
}

//###########################################################################

string process2(string s){
	return s;
}

//###########################################################################

/*
void testFunc(string s){
	RC_ASSERT( process(s) == process(s) );
};
*/

int main() {
	string s;
	int T;
	//check("TEST", testFunc);
	cin >> T;
	for(int l = 0 ; l < T ; l++) {
		int C, J;
		cin >> C >> J;
		vector<Task> v(C + J);
		for(int i = 0 ; i < C ; ++i){
			cin >> v[i].start >> v[i].end;
			v[i].o = c;
		}
		for(int i = 0 ; i < J ; ++i){
			cin >> v[C + i].start >> v[C + i].end;
			v[C + i].o = j;
		}
		//TRAITEMENT
		cout << "Case #" << l+1 << ": " << process(v) << endl;
		///////////
	}
	return 0;
}
