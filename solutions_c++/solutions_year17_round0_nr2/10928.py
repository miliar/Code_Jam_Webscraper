#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <cstring>
#include <iomanip>
#include <cmath>

#define ll long long
#define pb push_back
#define pii pair<int,int>
#define F first
#define S second
#define mp make_pair
#define endl  '\n'
#define pi acos(-1)
#define MOD 1000000007
#define MAX 1000005
#define INF 1000000000

using namespace std;
int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("C:/Users/GAURAV SUMAN/Desktop/input.txt", "r", stdin);
	freopen("C:/Users/GAURAV SUMAN/Desktop/output.txt", "w", stdout);

	int t;
	cin>>t;
	int cs=0;
	int st;
	while(t--){
    string str;
	cin >> str;
	//cout<<str<<endl;
	int n = str.length();
	cs++;
	int val = -1, idx = -1;
	for (int i = 0; i < n - 1; i++)
	{
		if (str[i] > str[i + 1])
		{
			idx = i;
			val = str[i + 1] - 48;
			break;
		}
	}
	cout<<"Case #"<<cs<<": ";
	if (idx == -1)
		cout << str << endl;
	else {

		string str1 = "";
		for (int i = 0; i < idx; i++)
			str1 += str[i];
		//    cout<<idx<<endl;
		//cout<<idx<<" "<<str1<<endl;
			int l = idx;
			 l--;
			 //cout<<str1<<endl;
			if(str[idx]==str[idx-1]){

			while (str[idx] == str[l] && l>=0) {
				//str1+= '9';
				l--;
			}
			if(l==-1 && str[0]=='1')
            {

                for(int i=0;i<n-1;i++)
                    cout<<9;
                cout<<endl;
                continue;
            }
			str1[l+1]=str[l+1]-1;
			for (int i = idx ; i < n; i++)
				str1 += '9';
			}
			else
            {
                if(l==-1 && str[0]=='1')
                {

                    for(int i=0;i<n-1;i++)
                    cout<<9;
                cout<<endl;
               continue;
                }
                str1+=str[l+1]-1;
                for (int i = idx+1 ; i < n; i++)
				str1 += '9';
            }

          //  cout<<str1<<endl;
			//cout<<str1<<endl;
            //cout<<l<<endl;
			//cout<<str1<<endl;

			cout << str1 << endl;
	}
	}
	return 0;
}
