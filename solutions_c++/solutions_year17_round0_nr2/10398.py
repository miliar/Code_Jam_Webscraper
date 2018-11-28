#include <iostream>
#include <string>
#include <sstream>
using namespace std;
long long sti(string a){
	long long b;
	stringstream lol;
	lol << a; lol >> b;
	return b;
}
string llts(long long b){
	string a;
	stringstream lol;
	lol << b;
	lol >> a;
	return a;
}
bool test(string a){
	for(int i = 0;i < a.length(); ++i)
		if(a[i] > a[i + 1] && i != a.length() - 1) return false;
	return true;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int a;
	scanf("%d", &a);
	for(long long i = 1; i <= a; ++i){
	    string b;
	    cin >> b;
	    long long prev = 0;
	    for(long long j = 1; j <= sti(b); ++j){
	    	if(test(llts(j))) prev = j;
		}
		printf("Case #%d: %lld\n",i,prev);
	}
	return 0;
}
