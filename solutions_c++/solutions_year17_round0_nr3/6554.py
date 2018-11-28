#include <bits/stdc++.h>
using namespace std;

void print(int ary[], int n){
	cout<<"\n";
	for (int i=0; i<n; i++){
		cout<<ary[i]<<"\t";
	}
	cout<<endl;
}

void initilise(int lAry[], int rAry[],int ary[], int n){
	for(int i=0; i<n; i++){
		if(ary[i]==1){
			lAry[i]=-1, rAry[i]=-1;
		}
		else{
			int ls=0, rs=0;
			for (int j=i-1; j>=0; j--){
				if(ary[j]==0) ls++;
				else if(ary[j]==1) break;
			}
			for (int j=i+1; j<n; j++){
				if(ary[j]==0) rs++;
				else if(ary[j]==1) break;
			}

			lAry[i]=ls;
			rAry[i]=rs;
		}
		//cout<<"bathroom no # "<<i+1<<"\t"<<lAry[i]<<"\t"<<rAry[i]<<endl;	
	}
}

int main(int argc, char const *argv[])
{
	int tc, x=0;

	string temp, temp1, temp2;

	fstream fin;
	fstream fout;

	fin.open("input.in",ios::in);
	fout.open("output.txt",ios::out);
	fin>>temp;

	stringstream convert(temp);
	convert>>tc;

	//cin>>tc;
	while(x<tc){
		int n, k;
		fin>>temp1>>temp2;
		stringstream convert1(temp1);
		convert1>>n;
		stringstream convert2(temp2);
		convert2>>k;
		//cin>>n>>k;
		int ary[n];
		for (int i=0; i<n; i++) ary[i]=0;

		int lAry[n];		//Put -1 for invalid bathroom i.e. occupied bathroom
		int rAry[n];		//Put -1 for invalid bathroom i.e. occupied bathroom

		int ans1, ans2;
		for(int i=0; i<k; i++){
			int p[n], q[n], ls, rs;			//store min of ls and rs in p and max of ls rs in q;
			initilise(lAry,rAry,ary,n);
			for (int j=0; j<n; j++){
				if(ary[j]==0){
					if (lAry[j]<rAry[j]) p[j]=lAry[j], q[j]=rAry[j] ;
					else if (lAry[j]>=rAry[j]) p[j]=rAry[j], q[j]=lAry[j];
				}
				else{
					p[j]=-1, q[j]=-1;
				}
				
			}
			//cout<<"The minimum of ls and rs value for each stall is"<<endl;
			//for (int j=0; j<n; j++) cout<<p[j]<<"\t";cout<<endl;
			//cout<<"The maximum of ls and rs value for each stall is"<<endl;
			//for (int j=0; j<n; j++) cout<<q[j]<<"\t";

			int temp1=-1000000, temp2=-1000000;
			for (int j=0; j<n;j++){
				if (temp1<p[j] && p[j]>=0) temp1=p[j];
				if (temp2<q[j] && q[j]>=0) temp2=q[j];
			}	

			//cout<<"\nThe maximum of min of ls and rs value is"<<temp1<<endl;
			//cout<<"\nThe maximum of max of ls and rs value is"<<temp2<<endl;
			vector<int> tie;
			for (int j=0; j<n; j++){
				if(p[j]==temp1 && ary[j]==0) tie.push_back(j);
			}
			if(tie.size()==1){
				//cout<<"resloved in case 1\n";
				int flag=tie[0];
				ary[flag]=1;
				ls=lAry[flag];
				rs=rAry[flag];
				//cout<<"New bathroom stall is\n";
				//print(ary, n);
			}
			else{
				//cout<<"tie 1 happened on \t";
				//for (int j=0; j<tie.size(); j++) cout<<tie[j]<<"\t";
				//cout<<endl;
				vector<int> tie2;
				int temp3=-10000000;
				for (int j=0; j<tie.size(); j++){
						//cout<<tie[j]<<endl;
						if(temp3<q[tie[j]]) temp3=q[tie[j]];
				}
				//cout<<"\nMaximum value among tie elements is\t"<<temp3;

				for (int j=0; j<tie.size(); j++){
						if(temp3==q[tie[j]]) tie2.push_back(tie[j]);
				}
				if(tie2.size()==0){
					//cout<<"resloved in case 2\n";
					ary[tie2[0]]=1;
					ls=lAry[tie2[0]];
					rs=rAry[tie2[0]];
				}
				else{
					//cout<<"\ntie 2 happened on\n";
					//for (int j=0; j<tie2.size(); j++) cout<<tie2[j]<<"\t";
					int flag=tie2[0];
					ary[flag]=1;
					ls=lAry[flag];
					rs=rAry[flag];
					//cout<<"New bathroom stall is\n";
					//print(ary, n);
				}
			}
			//cout<<"For "<<i+1<<"th person ls and rs value is \t"<<ls<<"\t"<<rs<<endl;
			if(ls<rs) ans1=ls, ans2=rs;
			else ans2=ls, ans1=rs;
		}
		fout<<"Case #"<<x+1<<": "<<ans2<<" "<<ans1<<endl;
		x++;

	}
	return 0;
}