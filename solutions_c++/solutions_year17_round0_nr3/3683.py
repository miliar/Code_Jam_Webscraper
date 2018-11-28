//#define LOCAL
#include<iostream>
#include<math.h>
typedef long long I64;
using namespace std; 
void countLevel(I64 k,int* level,I64* fatherCount){
	int lv=0;
	I64 sum=0;
	while(sum<k){
		sum+=pow(2,lv);
		lv++;
	}
	*level=lv-1;
	*fatherCount=sum-pow(2,lv-1);
}

int main()
{
	#ifdef LOCAL
	freopen("C-small-2-attempt0.in.txt","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		I64 n,k;
		cin>>n>>k;
		if(n<=k){
			cout<<"0 0"<<endl;
			continue;
		}
		// int level = log10(k)/log10(2);
		// I64 fatherCount= (level!=0)?pow(2,level-1):0;//how many before k
		int level;
		I64 fatherCount;
		countLevel(k,&level,&fatherCount);
		// cout<<level<<" "<<fatherCount<<endl;
		k-=fatherCount;// kth in this level
		//build the index for each level
		I64 len1[level+1],len2[level+1],count1[level+1],count2[level+1];
		len1[0]=len2[0]=n;
		count1[0]=1;count2[0]=0;
		for(int lv=1;lv<level+1;lv++){
			I64 left1,right1,left2,right2;
			if(len1[lv-1]%2==1)left1=right1=(len1[lv-1]-1)/2;
			else{
				left1=floor((len1[lv-1]-1)/2);
				right1=floor((len1[lv-1]-1)/2)+1;
			}
			if(len2[lv-1]%2==1)left2=right2=(len2[lv-1]-1)/2;
			else{
				left2=floor((len2[lv-1]-1)/2);
				right2=floor((len2[lv-1]-1)/2)+1;
			}
			//update the results for this level
			count1[lv]=count1[lv-1],count2[lv]=0,len1[lv]=len2[lv]=left1;
			if(left1==right1)count1[lv]+=count1[lv-1];else{count2[lv]+=count1[lv-1];len2[lv]=right1;}
			if(left1==left2)count1[lv]+=count2[lv-1];else{count2[lv]+=count2[lv-1];len2[lv]=left2;}
			if(left1==right2)count1[lv]+=count2[lv-1];else{count2[lv]+=count2[lv-1];len2[lv]=right2;}
			// cout<<"lv"<<lv<<":"<<left1<<" "<<right1<<" "<<left2<<" "<<right2<<endl;
		}
		//judge the count
		// cout<<"final:"<<len1[level]<<" "<<len2[level]<<" "<<count1[level]<<" "<<count2[level]<<endl;
		if((len1[level]>=len2[level]&&count1[level]>=k)||(len1[level]<=len2[level]&&count2[level]>=k)){
			if(len2[level]%2==1)len1[level+1]=len2[level+1]=(len2[level]-1)/2;
			else if(len2[level]==0){cout<<"0 0"<<endl;continue;}
			else{
				len1[level+1]=floor((len2[level]-1)/2);
				len2[level+1]=floor((len2[level]-1)/2)+1;
			}
		}
		else{
			if(len1[level]%2==1)len1[level+1]=len2[level+1]=(len1[level]-1)/2;
			else if(len1[level]==0){cout<<"0 0"<<endl;continue;}
			else{
				len1[level+1]=floor((len1[level]-1)/2);
				len2[level+1]=floor((len1[level]-1)/2)+1;
			}
		}
		if(len1[level+1]>len2[level+1])cout<<len1[level+1]<<" "<<len2[level+1]<<endl;
		else cout<<len2[level+1]<<" "<<len1[level+1]<<endl;
	}
	return 0;
}
