#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,rd=1;
	cin>>n;
	while(n--){
		string cad,aux="";
		int k;
		cin>>cad>>k;
		for (int i = 0; i < cad.size(); ++i)
			aux=aux+'+'+"";
		int cd=0,res=0;
		int index=0;
		while(cd==0){
			if(cad[index]==aux[index]){
				index++;
				if(index==cad.size())
					break;
			}
			else{
				if(k+index<=aux.size()){
					res++;
					for (int i = index; i < k+index; ++i){
						if(aux[i]=='-')
							aux[i]='+';
						else
							aux[i]='-';
					}
				}
				else{
					break;
				}
			}
		}
		if(cad==aux)
			cout<<"Case #"<<rd<<": "<<res<<endl;
		else
			cout<<"Case #"<<rd<<": "<<"IMPOSSIBLE"<<endl;
		rd++;
	}
	system("pause");
	return 0;
}