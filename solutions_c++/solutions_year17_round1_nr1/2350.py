#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define M 1000000007
#define MAXN 112345
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out_large.txt", "w", stdout);
    const char QUES = '?';
    int i, j, r, c, T;
    cin>>T;
    for(int t = 1; t <= T; t++) {
        string s[30];
	    cin>>r>>c;
	
	    for(i = 1 ;i <= r; i++) {
	        cin>>s[i];
	        s[i] = '#' + s[i];
            
	    }
	    int flag = 0, last_pos, global_flag = 0, first_row = -1;
	    for(i = 1; i <= r; i++) {
	        flag = 0;
	        last_pos = 1;
	        for(j = 1; j <= c; j++) {
	            if(s[i][j] == QUES) {
	                continue;
	            }
	            else {
	                global_flag = 1;
	                for(int k = last_pos; k < j; k++) {
	                    s[i][k] = s[i][j];
	                }
	                last_pos = j + 1;   
	            }
	
	
	            if(global_flag == 1 && first_row == -1) {
	                first_row = i;
	            }
	            flag = 1;
                //cout<<"last_pos:"<<last_pos<<endl;
                //cout<<s[i]<<endl;
	        }
            
            if(last_pos != c + 1) {
                for(int k = last_pos; k <= c; k++) {
                    s[i][k] = s[i][last_pos - 1];
                }
            }
	        if(flag == 0 && i != 1) {
	            for(j = 1; j <= c; j++) {
	                s[i][j] = s[i - 1][j];
	            }
	        }
            //cout<<flag<<" "<<global_flag<<" "<<first_row<<endl;
	    }
	
	    for(i = first_row - 1; i >= 1; i--) {
	        for(int j = 1; j <= c; j++) {
	            s[i][j] = s[first_row][j];
	        }
	    }

        cout<<"Case #"<<t<<":"<<endl;    
	    for(i = 1; i <= r; i++) {
	        for(j = 1; j <= c; j++) {
	            cout<<s[i][j];
	        }
	        cout<<endl;
	    }
    }

}

