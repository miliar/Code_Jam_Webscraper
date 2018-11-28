/*
																									 
											 `-:://:::-                                             
										   `//:-------:/:`                                          
										  .+:--.......--:+`                                         
										 `+:--..`````..--//`                                        
										 .o:--..`` ``..--:o`                                        
										 .o:--...```..---+/`                                        
									   `/y+o/---....---:+o.                                         
								   `...````-os+/:---:/+o/--.`                                       
			  `-/+++++/:.      `...`       :h+d+oooo+/+-`   ...                                     
			`/++//:::://++-`....`         -.`//````````:`     `..`                                  
		   `o+/::------://o/`           `-` -.          -`       `..`                               
 `---.-o/:./o/::-..``..-ЗАПУСКАЕМ      ..  ..            -`        `...       ``..``                
  `....o+:-++/:--.```..-://s.        `-`  .-              -`          `-o: .-//::::/:-`             
		  `:s+/:--....-::/+s-`      .-   `-                -`           -///:--------:/:`           
		   ./s+//:::::://oo-``..НЕЙРОННУЮ: СЕТЬ:::::::-`РАБОТЯГИ        `+:--........--:/`          
			.:ooo+++++osso-`    `.:-...`/` ./::-------:/:`   -`         :+--..``````.--:+:...-+:-`  
			 `.-/+++++/+-.-`    -.   ``:so:/:--.......--:+`  `-```````o+/+--..`````..--:o/-..:s+:.  
				 ```````:``.. `-`     -` `+:--..`````..--/+-.../.`````..-o:--.......---/o.    `     
						`:  `:-      -.  .o:--..`` ``..--:o`   `-`      `:o+:--------:+o-`          
						 `-`-...    ..   .o/--...```..--:+/`    `-`     `oy/so/////++o/.`           
						  -/`  `-` `- ``+s/o/:---...---:++.      `-`   .-../d://///:-.`             
				`.---..``-..-    .-/..`````-oo+/:::::/+o+-        `-``-`  `-.  ````                 
			 `:++++/+++++-  ..``.-/:`      /y-:/++o++/:.`..`       ./.   `-                         
			-++/::::::://+/..:-``:` ..   `-.`  ```.```    `..`   `..`-` `-                          
	   ``  -o//:--....-::/++` -.-`   `-`.-`                 `..`..`  `-.-                           
  -----ss+:++/:--.```..-://s.  /.     `::                    `-:.     ./`                           
  `````/:..+o/::-..``.--:/+s. ..-`   `-``-`                 ..` `-`  `-`-`                          
		  `-s+/::-----::/+oo---``-` ..    .:-    ```      .-`     .-.-  `-`                         
		   `:oo+//::://+os/..:`..-/:`      :y.-:::::::.`.-`        ./-`  `-`                        
			`./+oooooooo+/.`-    .-:...`.. .//:-------://`        `- `..` `:.                       
			  ``.-::::-.``-/`  `-` `-  `oo:+:--.......--:/`      `-    `.:--h.``..```               
						  -.-`.-    .-   `+:--..`````..--//`    `-       /s-//::::::::.             
						 -` `/-      ..  .o:--..`` ``..--:o.```.-        `//:--------://`           
						-` .-`.-`     -.`-o/--...```..--:+/.``-:....``:-.+:--....`...--:+`          
					   ..`-.   `-.   ``:os:o/:---...---:++.  `-     ``///+:-..``````.--:+-````-.`   
			  `.:///////.-`      .:-..` -``-+o+/:::::/+o/.  `-         `:+:-..`````..--:o/:--/ys+-  
			`-++///////+o/. ``....`-.    :` `.:++++++/:.`  .-           -o/---......---/o.   `.`    
		   `++//:-----::/+o:..`     .-`   :    ```````    .-           `+so+:--------:++-`          
  `````:-``:o/::-..`..--:/+o`         -.  `-             .-          `../../+o+////+o+:.`           
  -----syo/o+/:--.```..-://s.          .-` `-           .-        `...     ``-:////:-``             
	   .` `/s//:--....-::/+s.            -. `-`        .-       `..`                                
		   .+o+/:::--:://+s/-..`          .::+y  ```  .-     `..`                                   
			./oo++////+oso-`   `....       :y-+:::::::/`   ...                                      
			 `.:+oooooo/-`         `....-. .//:-------:/:-.`                                        
				``...``                 /+:+:--.......--:+`                                         
										 `+:--..`````..--//`                                        
										 .o:--..`` ``..--:o`                                        
										 .+/--...```..--:+/`                                        
										 `-o/:---...---:++.                                         
										  `-+o+/:---:/+o/.                                          
											`.:+oooo+/-.`                                           
											   ``````                                               
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <ostream>
#include <istream>
#include <typeinfo>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <limits>
#include <fstream>
#include <array>
#include <list>
#include <bitset>
#include <functional>

#define mt make_tuple
#define x first
#define y second
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define mp make_pair
#define umap unordered_map
#define uset unordered_set
#define rt return 0;
#define elif else if
#define len(v) ((int)v.size())


using namespace std;

char string_in_buffer[(int)2e5];


void fast_scan(int &x) { scanf("%d", &x); }
void fast_scan(long long &x) { scanf("%lld", &x); }
void fast_scan(unsigned long long &x) { scanf("%llu", &x); }
void fast_scan(double &x) { scanf("%lf", &x); }
void fast_scan(long double &x) { scanf("%Lf", &x); }
void fast_scan(char &x) { 
	scanf("%c", &x); 
	if (x == '\n') {
		fast_scan(x);
	}
}
void fast_scan(string &x) {
	scanf("%s", string_in_buffer);
	x = string(string_in_buffer);
}

template<class TFirst, class TSecond>
void fast_scan(pair<TFirst, TSecond> &p) {
	fast_scan(p.first);
	fast_scan(p.second);
}

template <class T>
void fast_scan(vector<T> &v) {
	for (auto &x : v) fast_scan(x);
}

void fast_print(const int &x) { printf("%d", x); }
void fast_print(const long long &x) { printf("%lld", x); }
void fast_print(const unsigned long long &x) { printf("%llu", x); }
void fast_print(const double &x) { printf("%.15lf", x); }
void fast_print(const long double &x) { printf("%.15Lf", x); }
void fast_print(const char &x) { printf("%c", x); };
void fast_print(const string &x) { printf("%s", x.c_str());}

template<class TFirst, class TSecond>
void fast_print(const pair<TFirst, TSecond> &p) {
	fast_print(p.first);
	fast_print(' ');
	fast_print(p.second);
}

template <class T>
void fast_print(const vector<T> &v) {
	if (v.empty()) return;
	fast_print(v[0]);
	for (int i = 1; i < v.size(); i++) {
		fast_print(" ");
		fast_print(v[i]);
	}
}

template <class T>
void fast_print(const vector<vector<T>> &v) {
	if (v.empty()) return;
	fast_print(v[0]);
	for (int i = 1; i < v.size(); i++) {
		fast_print("\n");
		fast_print(v[i]);
	}
}



using namespace std;


namespace smart_io {
	string print_start = "";
	string sep = " ";
	bool first_print = false;

	void precall_print() {
		fast_print(print_start);
		print_start = "\n";
		first_print = true;
	}
} //namespace smart_io


template <class T>
ostream &operator,(ostream &os, const T &object) {
	if (!smart_io::first_print) {
		fast_print(smart_io::sep);
	} else {
		smart_io::first_print = false;
	}
	fast_print(object);
	return os;
}

template <class T>
istream &operator,(istream &is, T &object) {
	fast_scan(object);
	return is;
}

namespace typedefs {
	typedef long long ll;
	typedef unsigned long long ull;
	typedef pair<int, int> pii;
}

namespace numbers_operation {
	template<class T>
	T floor_mod(T a, T b) {
		if (a % b == 0) return 0;
		if (a >= 0 && b >= 0) return a % b;
		if (a <= 0 && b <= 0) return a % b;
		return abs(b) - (abs(a) % abs(b));
	}
}

using namespace numbers_operation;
using namespace typedefs;

#define print    \
smart_io::precall_print(); \
cout,

#define scan cin,



string base;
string rez;

string zip(const string &s) {
	string rez = "";
	int iter = 0;
	while (iter < len(s) && s[iter] == '0') {
		iter++;
	}

	while (iter < len(s)) {
		rez += s[iter];
		iter++;
	}
	if (rez.empty()) return "0";
	return rez;
}


int get(int id) {
	return base[id] - '0';
}

map<tuple<int, int, int>, bool> dp;

bool can(int i, int _min, bool can_ovf) {
	auto t = mt(i, _min, can_ovf);
	if (dp.find(t) != dp.end()) return dp[t];
	if (i == len(base)) {
		return dp[t] = true;
	} else {
		int right;
		if (can_ovf) {
			right = 9;
		} else {
			right = get(i);
		}
		for (int c = right; c >= _min; c--) {
			bool sub_ovf = can_ovf || (c < get(i));
			if (can(i + 1, c, sub_ovf)) {
				rez[i] = '0' + (char)c;
				return dp[t] = true;
			}
		}
	}
	return dp[t] = false;
}

signed main(signed argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cnt_tests;
	scan cnt_tests;

	for (int test = 0; test < cnt_tests; test++) {
		scan base;
		dp.clear();
		rez = base;
		can(0, 0, false);
		print ("Case #" + to_string(test + 1) + ":"), zip(rez);
	}
}