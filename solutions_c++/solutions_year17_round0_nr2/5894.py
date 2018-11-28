#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>


using namespace std;

vector<int> to_vec(long long n){
	int r = 0;
	vector<int> v;
	while(n > 0){
		r = n%10;
		v.push_back(r);
		n /= 10;
	}
	reverse(v.begin(), v.end());
	return v;
}

void print_vector(vector<int> c){
	for (int i = 0; i < c.size(); ++i)
	{
		cout << c[i];
	}
	cout << endl;
}

bool fixed(long long n){
	vector<int> c = to_vec(n);
	for (int i = 0; i < c.size() - 1; ++i)
	{
		if(c[i] > c[i+1]){
			return false;
		}
	}
	return true;
}

long long to_int(vector<int> c, int k){
	long long n = c[k];
	for (int i = k+1; i < c.size(); i++)
	{
		n = n*10 + c[i];
	}
	return n;
}

int main(){
	long long T, k;
	cin >> T;
	int counter = 0;
	long long n;
	while(T--){
		cin >> n;
		while(!fixed(n)){
			vector<int> c = to_vec(n);
			for (int i = 0; i < c.size() - 1; ++i)
			{
				if(c[i] > c[i+1]){
					k = i;
					while( k > 0 && c[k-1] == c[k]) k--;
					long long sub = to_int(c, k+1) + 1;
					
					n -= sub;
					break;
				}
			}
		}
		counter++;
		cout << "Case #" << counter << ": " << n << endl;
	}
	return 0;
}