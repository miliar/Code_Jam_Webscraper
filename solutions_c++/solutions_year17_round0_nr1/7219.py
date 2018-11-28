#include <iostream>

using namespace std;

int main()
{
int t;
cin >> t;
for(int i=1;i<=t;i++){
	string a; int k;int count = 0;
	int flag = 0;
	cin >> a >> k;
	for(int j=0;j<a.size();j++){
	if(a[j]=='-'){
	if(j+k>a.size()){
		flag = 1;
		break;
	}
	else
	{ 
	count ++;
	for(int l=0;l<k;l++){
		if(a[j+l]=='-')
			a[j+l]='+';
		else
			a[j+l]='-';
	}
	}
}
}
if(flag)
cout << "Case #"<<i<<": IMPOSSIBLE\n";
else
cout << "Case #"<<i<<": "<<count<<"\n";
}
}
