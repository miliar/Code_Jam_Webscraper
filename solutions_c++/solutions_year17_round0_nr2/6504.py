#include<iostream>
#include<climits>
using namespace std;

int main() {
    int T,i,j,k,t,len;
    bool flag;
    long long N;
    int arr[20], ans[20];
    cin>>T;
    for (t=1; t<=T; t++) {
        cin>>N;
	flag = false;
	len=0;
	while (N>0) {
            arr[len++] = N%10;
            N/=10;
	}
	i=len-1;
	j=0;
	while(i>=0) {
	    // find next diff num
	    // if small then reduce this digit and make all next as 9
	    // else move to the next digit
	    k=i;
	    while (k>=0 && arr[k]==arr[i]) k--;
	    if (k==-1 || arr[i]<arr[k]) {
		//cout<<i<<" "<<k<<endl;
	    	for (; i>k; i--) ans[j++] = arr[i];
	    } else {
		//cout<<i<<" "<<arr[i]-1<<endl;
	    	ans[j++]=arr[i]-1;
		i--;
		for(;i>=0;i--) ans[j++]=9;
	    }
	}
	cout<<"Case #"<<t<<": ";
	for(i=0; i<j; i++) if (i>0 || ans[i]!=0) cout<<ans[i];
	cout<<endl;
    }
    return 0;
}
