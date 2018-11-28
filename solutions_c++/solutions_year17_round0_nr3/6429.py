#include <iostream>

using namespace std;

long long bathroom(long long number, long long index) {
	if (index == 1) {
		return number;
	} else {
		number = number-1;
		if (index % 2 == 1) {
			return bathroom(number/2, index/2);
		} else {
			return (number % 2) == 0 ? bathroom(number/2, index/2) : bathroom(number/2 + 1, index/2);
		}
	}
}

int main()
{
    long long number, k;
    long long min, max;
    int t;
    int tcase;
    tcase = 1;

    cin>>t;

    while(t--) {
    	cin >> number >> k;
    	number = bathroom(number, k);
    	number = number - 1;

    	min = number/2;
    	max = (number % 2) == 0 ? number/2 : number/2 + 1;

    	cout << "Case #" << tcase++ << ": " << max << " " << min << endl;
    }

    return 0;
}