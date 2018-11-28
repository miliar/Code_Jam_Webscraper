#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

	//input
	//---------------------

		//the number of test cases
		int T;

		//input data
		string in[100];

		//output data
		int Out[100];

		int K[100],S=0,Count=0,Count_P=0;
		string str;
 
		cin >> T;

		for(int i=0; i<T; i++){
			cin >> in[i];
			cin >> K[i];
		}

		//cout << "T" << T << endl;
		//for(int i=0; i<T; i++){
			//cout << "Case"<< i+1 << ":" << in[i] << endl;
		//}

	//---------------------

	for(int i=0; i<T; i++)
	{

		str = in[i];

		//cout<< "Case#" << i+1 << endl;
		//cout<< "str: " << str << endl;

		//—v‘f”S
		S = str.size();
		//cout<< "S: " << S << endl;

		//cout<< "K: " << K[i] << endl;

		//Count_P
		for(int j=0; j<S; j++)
		{
			//cout<< "str["<< j << "]" << str[j] << endl;
			if(str[j]=='+')
			{
				Count_P++;
			}
		}
		//cout<< "Count_P: " << Count_P << endl;
		//cout<< Count <<" : "<<"str:" << str << endl;
		int flag=0;
		while( Count_P < S )
		{

			//ˆ—
			for(int j=S-1; -1<j; j--)
			{
				if(str[j]=='-')
				{
					if( j < K[i]-1 ){
						flag=1;
						break;
					}

					int l=j;
					int flip = 0;
					while(flip < K[i])
					{
						if(str[l]=='-')
						{
							str[l]='+';
						}
						else if(str[l]=='+')
						{
							str[l]='-';
						}
						flip++;
						l--;
					}
					break;
				}
			}
			if(flag==1){
				break;
			}
			Count++;
			//cout<< Count <<" : "<<"str:" << str << endl;

			//Count_PXV
			Count_P=0;
			for(int j=0; j<S; j++)
			{
				if(str[j]=='+')
				{
					Count_P++;
				}
			}
		}
		if(flag==1){
			Out[i]=-1;
		}else{
			Out[i]=Count;
		}
		flag=0;
		Count=0;
		Count_P=0;
		str.empty();
		//cout<<endl;
	}

	//output
	//---------------------
	for(int i=0; i<T; i++){
		if(i<T-1){
			if(Out[i]==-1){
				cout << "Case #" << i+1 << ": "<< "IMPOSSIBLE" << endl;
			}else{
				cout << "Case #" << i+1 << ": "<< Out[i] << endl;
			}
		}else{
			if(Out[i]==-1){
				cout << "Case #" << i+1 << ": "<< "IMPOSSIBLE";
			}else{
				cout << "Case #" << i+1 << ": "<< Out[i];
			}
		}
	}

	//---------------------

    	return 0;
}
