#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin("B-small-attempt0.in");
	//ifstream fin("A-large.in");
	ofstream fout("B-small-attempt0.out");
	//ofstream fout("A-large.out");    
    int T;
    fin >> T;
      
    int N, C, M;
    int P[1001];
    int B[1001];
    int count_p[1001];
    int count_b[1001];
		
    for (int t = 1 ; t <= T; t++)
    { 
    	fin >> N >> C >> M;
    	
    	for (int i = 0 ; i < 1001 ; i++) {
    		count_p[i] = 0;
    		count_b[i] = 0;
		}
    	for (int i = 0 ; i < M ; i++) {
    		fin >> P[i] >> B[i];
    		count_p[P[i]]++;
    		count_b[B[i]]++;
		}
		/*
		for (int i = 1; i <= N ; i++) {
			cout << count_p[i] << " ";
		}
		cout << endl;
		for (int i = 1; i <= C ; i++) {
			cout << count_b[i] << " ";
		}
		cout << endl;
		*/
 		int max_b = 0;
		int ans_b = 0;
		int idx = 0;
		for (int i = 1 ; i <= C ; i++) {
			if (max_b < count_b[i]) {
				max_b = count_b[i];
				idx = i;
			}
		}
		for (int i = 1 ; i <= N ; i++) {
			if (count_p[i] > max_b)
				ans_b += count_p[i]-max_b;
		}
		cout << max_b << " " << idx << " " << ans_b << endl;
		int max_p = 0;
		int ans_p = 0;
		for (int i = 1 ; i <= N ; i++) {
			int temp = count_p[i] - max_p;
			int add_max = (temp+i-1)/i;
			max_p += add_max;
			if (temp > add_max)
			ans_p += temp-add_max;
		}
		cout << max_p << " " << ans_p << endl << endl;
		if (max_p > max_b) {
			fout << "Case #" << t << ": " << max_p << " " << ans_p << endl;
		} else {
			fout << "Case #" << t << ": " << max_b << " " << ans_b << endl;
		}
    	
	}
}

