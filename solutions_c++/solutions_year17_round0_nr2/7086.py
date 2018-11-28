#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;
main()
{
	ifstream file;
	ofstream outs;
	file.open("doc3.txt");
	outs.open("out.txt");
	int t;
	file>>t;
	//cin>>t;
	int tc=1;
	while(t--)
	{
		string n;
		file>>n;
		//cin>>n;
		if(n.length()==1)
		{
//		cout<<"Case #"<<tc++<<": ";
//			cout<<n<<endl;
		outs<<"Case #"<<tc++<<": ";
			outs<<n<<endl;
			continue;
		}
		int pos=-1;
		for(int i=0;i<n.length()-1;i++)
		{
			if(n[i+1]<n[i])
			{
				pos=i;
				break;
			}
		}
	   if(pos==-1)
	   {
//	   	cout<<"Case #"<<tc++<<": ";
//		cout<<n;
//	   	cout<<endl;
        outs<<"Case #"<<tc++<<": ";
		outs<<n;
	   	outs<<endl;
	   	continue;
	   }
	   while(pos!=0&&n[pos]==n[pos-1])
	   {
	   	pos--;
	   }
	   n[pos]=n[pos]-1;
	   for(int i=pos+1;i<n.length();i++)
	   n[i]=57;
	   if(n[0]==48)
	   {
        //cout<<"Case #"<<tc++<<": ";
	   	outs<<"Case #"<<tc++<<": ";
		for(int i=1;i<n.length();i++)
//        cout<<"9";
//	   	cout<<endl;
	   	outs<<"9";
	   	outs<<endl;
	   }
	   else
	   {
//       cout<<"Case #"<<tc++<<": ";
//	   cout<<n;
//	   cout<<endl;
	   outs<<"Case #"<<tc++<<": ";
	   outs<<n;
	   outs<<endl;
}
	}
}
