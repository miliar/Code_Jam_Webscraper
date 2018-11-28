#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool isTidy(const vector<int>& v)
{
	int i=0;
	while(i<v.size()-1){
	   if(v[i] > v[i+1])
	    return false;
	 i++;
	}
  return true;
}

int formInt(const vector<int>& v)
{
	int i=0,j=0;
	while(j<v.size())
	   i=i*10+v[j++];

	return i;
}

void changeTidy(vector<int>& v)
{
	int i=0;
	if(v.size() ==1 || isTidy(v))
		return;

    	while((i<v.size()-1) && v[i]<v[i+1])
    		i++;
        
        if(i < v.size()-1)
        v[i]=v[i]-1;
        i++;

        while(i<v.size())
               v[i++]=9;
}

int main(){
    vector<int> v;
    int t,c=0,n;
    cin >> t;

    while(t--){
    	c++;
    	cin >> n;

    	while(n){
    		v.push_back(n%10);
    		n/=10;
    	}

    	reverse(v.begin(),v.end());
        changeTidy(v);
        cout <<"Case #" << c <<": " << formInt(v) << endl;
        v.clear();
    }
	return 0;
}