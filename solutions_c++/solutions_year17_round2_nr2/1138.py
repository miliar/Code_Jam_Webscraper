//input and output
#include <iostream>
#include <iomanip>
#include <fstream>
//working with strings
#include <cstring>
#include <sstream>
//debugging with assert
#include <cassert>
//datastructures
#include <deque>
#include <list>
#include <set>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
//math operations and pairs, rand, atoi, atof and standard stuff
#include <cstdlib>
#include <cmath>
#include <numeric>
//for sorting and other stuff
#include <algorithm>

template <typename T>
std::ostream& operator<<(std::ostream& os, std::deque<T> vector);

template <typename S, typename T>
std::ostream& operator<<(std::ostream& os, std::pair<S,T> pa);

template <typename T>
std::ostream& operator<<(std::ostream& os, std::deque<T> vector){
	if(vector.size()==0)
		return os;
	os << vector[0];
	for(unsigned long long i=1;i<vector.size();++i)
		os << std::endl << vector[i];
	return os;
}

template <typename S, typename T>
std::ostream& operator<<(std::ostream& os, std::pair<S,T> pa){
	os << pa.first << " " << pa.second;
	return os;
}

//goes through the selection possibilites of k elements of the vector
//use: ++si for next selection and *si for a vector of the currently selected elements
//use: for(SelectionIterator<T> si(vector,k);!si.final();++si){something with *si}
template <typename T>
class SelectionIterator{
private:
	unsigned long long k;
	unsigned long long n;
	std::deque<T> vector;
	std::deque<T> selection;
	std::deque<unsigned long long> selectionNumbers;
	bool finalState;
public:
	SelectionIterator<T>(std::deque<T> vector, unsigned long long k):k(k), n(vector.size()), vector(vector), finalState(false){
		for(unsigned long long i=0;i<k;++i){
			selection.push_back(vector[i]);
			selectionNumbers.push_back(i);
		}
	}

	void operator++(){
		for(unsigned long long i=k-1;i<k;--i){
			if(selectionNumbers[i]==n+i-k)
				continue;
			else{
				++selectionNumbers[i];
				selection[i]=vector[selectionNumbers[i]];
				for(unsigned long long j=i+1;j<k;++j){
					selectionNumbers[j]=selectionNumbers[i]+j-i;
					selection[j]=vector[selectionNumbers[j]];
				}
				return;
			}
		}
		finalState=true;
	}

	std::deque<T> operator*(){
		return selection;
	}

	bool final(){
		return finalState;
	}
};
#define seliter SelectionIterator

//select from elements, indicated by the ones "1" in the binary representation
template <typename T>
std::deque<T> getSelection(std::deque<T> elements, unsigned long long binaryRepresentationOfSelection){
	std::deque<T> result;
	for(unsigned long long i=0;i<elements.size();++i)
		if( (binaryRepresentationOfSelection>>i)%2 )
			result.push_back(elements[i]);
	return result;
}
#define gsel getSelection

//calculating faculty of n, only valid for n<=20
unsigned long long facll(unsigned long long n){
	if(n)
		return n*facll(n-1);
	return 1;
}

//calculating faculty of n, floating point calulations
long double facld(unsigned long long n){
	if(n)
		return (long double)n * facld(n-1);
	return 1.;
}

//calculating the power of base to the exp
long long powll(long long base, unsigned long long exp){
	long long result=1;
	for(unsigned long long i=0;i<exp;++i)
		result*=base;
	return result;
}

//calculating the binary log of n
unsigned long long log2ll(unsigned long long n){
	assert(n>0);
	if(n==1)
		return 0;
	return 1+log2ll(n>>1);
}

using namespace std;

typedef long long ll;
typedef long double ld;
typedef string str;

#define mp make_pair
#define x first
#define y second
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define hash unordered_map
#define sz size()
#define bn begin()
#define ed end()

#define v(type) deque<type >
#define p(type1,type2) pair<type1, type2 >
#define it(container) typeof((container).begin())
#define all(x) (x).begin(), (x).end()
#define select(x,i) (x).begin()+(i), (x).begin()+(i)+1
#define foreach(cit,container) for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); cit++)
#define foreachc(c,cit,container) ll c=0;for(typeof((container).begin()) cit = (container).begin(); cit != (container).end(); c++, cit++)
#define forn(i, n) for (ll i = 0; i < (ll)(n); ++i)
#define fornn(i, a, b) for (ll i = (ll)(a); i < (ll)(b); ++i)
#define fore(i, a, b) for (ll i = (ll)(a); i <= (ll)(b); ++i)

#define inf 9000000000000000000L
#define eps 1e-15
#define pi 3.14159265358979323846264338328L

void init(){
}

str small(ll N, ll r, ll y, ll b){
	ll half = N/2;
	if(r>half)
		return "";
	if(y>half)
		return "";
	if(b>half)
		return "";

	str result(N,' ');
	v(ll) s;
	s.pb(r);
	s.pb(y);
	s.pb(b);
	sort(all(s));
	for(ll i=0;i<N;i+=2){
		result[i]=s.sz+'0';
		s.back()-=1;
		if(s.back()==0)
			s.popb();
	}
	for(ll i=1;i<N;i+=2){
		result[i]=s.sz+'0';
		s.back()-=1;
		if(s.back()==0)
			s.popb();
	}

	v(p(ll,char)) st;
	st.pb(mp(r,'R'));
	st.pb(mp(y,'Y'));
	st.pb(mp(b,'B'));
	sort(all(st));

	forn(i,N){
		result[i]=st[result[i]-'1'].y;
	}

	return result;
}

typedef str otype;
otype calcFunction(ll n, ll R, ll o, ll Y, ll g, ll B, ll v) {
	str result;
	ll r=R-g;
	ll y=Y-v;
	ll b=B-o;
	ll N = r+y+b;
	if(N==0 && R==0 && Y==0 && b==0){
		result="";
		forn(i,B){
			result+="BO";
		}
		return result;
	}
	if(N==0 && R==0 && y==0 && B==0){
		result="";
		forn(i,Y){
			result+="YV";
		}
		return result;
	}
	if(N==0 && r==0 && Y==0 && B==0){
		result="";
		forn(i,R){
			result+="RG";
		}
		return result;
	}
	str smallStr = small(N,r,y,b);
	while(o>0){
		--o;
		ll f=smallStr.find("B");
		smallStr.insert(f,"BO");
	}
	while(g>0){
		--g;
		ll f=smallStr.find("R");
		smallStr.insert(f,"RG");
	}
	while(v>0){
		--v;
		ll f=smallStr.find("Y");
		smallStr.insert(f,"YV");
	}
	return smallStr;
}

#define IFSTRUCT	//remove comment on this line, to activate if-structure for default value trigger
int main() {
	init();
	ofstream outfile("output.txt");
	cout << setprecision(10);
	outfile << setprecision(10);
	ll tests = 0;
	cin >> tests;
	fore(test, 1, tests){
		//read input
		ll n, R, o, Y, g, B, v;
		cin >> n >> R >> o >> Y >> g >> B >> v;
		//calc result
		otype result=calcFunction(n, R, o, Y, g, B, v);
		//write output
		outfile << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";
#ifndef IFSTRUCT
		outfile << result << endl;
		cout << result << endl;
#endif /*IFSTRUCT*/
#ifdef IFSTRUCT
		if(result.sz>0){
			outfile << result << endl;
			cout << result << endl;
		}
		else{
			str errorWord = "IMPOSSIBLE";
			outfile << errorWord << endl;
			cout << errorWord << endl;
		}
#endif /*IFSTRUCT*/
	}
	outfile.close();
	return 0;
}
