#include "iostream"
#include "algorithm"
#include "cstring"

using namespace std;

typedef long long ll;

const size_t LIMIT = 10e6;
int k;
char s[LIMIT + 5];

void flip(int i)
{
	for(int j = 0; j < k; ++j) {
		s[i+j] = (s[i+j] == '+'? '-':'+'); 
	}
	return;
}

bool allHappy() 
{
	for(int i = strlen(s)-1, j = 0; j < k; ++j, --i) {
		if(s[i] == '-') {
			return false;
		}
	}
	return true;
}

int main() {
	int T; cin >>T;
	
	for(int cs = 1; cs <= T; ++cs) {
		cin >>s >>k;

		int l = strlen(s) - k;
		int f{0};
		for(int i = 0; i <= l; ++i) {
			if(s[i] == '-') {
				flip(i);
				f++;
			}
		}

		if(allHappy()) {
			cout <<"Case #" <<cs <<": " <<f <<endl;
		} else {
			cout <<"Case #" <<cs <<": IMPOSSIBLE\n";
		}
	}

	return 0;
}
	
		
