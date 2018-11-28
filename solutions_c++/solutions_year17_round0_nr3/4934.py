#include <iostream>
#include <queue>
using namespace std;


struct Segmento
{
	long long int first;
	long long int second;
	
	Segmento(long long int L, long long int pos){
		this->first=L;this->second=pos;
	}
	Segmento(){}
	void operator=(const Segmento& seg){
        this->first = seg.first;
        this->second = seg.second;
    }

	bool operator<(const Segmento &seg) const{
		return ( this->first<seg.first || ((this->first==seg.first) && this->second>seg.second ));
	}
	bool operator<=(const Segmento &seg) const{
		return ( (*this)<seg || (*this)==seg );
	}
	bool operator==(const Segmento &seg) const{
		return (this->first==seg.first && this->second==seg.second); 
	}
};
void print_seg(Segmento &seg1){
	cout << "("<<seg1.first << ", "<< seg1.second << ")";
}
void partir_Segmento(Segmento &seg1,Segmento &seg2){
	
	//cout << "Sale ";print_seg(seg1);cout<<endl;
	
	if( seg1.first%2 == 0 )// par
	{
		seg1.first = seg1.first/2 -1;
		seg2.first = seg1.first + 1;
		//seg2.second = seg1.second + seg1.first + 1; 
	}
	else
	{//impar y mayor que 1
		seg1.first = seg1.first/2;
		seg2.first = seg1.first;
	}
	seg2.second = seg1.second + seg1.first + 1; 
	
	//cout << "Parti en ";print_seg(seg1);cout << " y ";print_seg(seg2);cout <<endl;
	return ;
}

//cola de pares(longitud,inicio) ambos enteros
void resolver(long long int N, long long int K){
	priority_queue<Segmento> segmentos;
	Segmento seg1(N,0),seg2;

	//cout<<"inicial ";print_seg(seg1);cout<<endl;
	
	segmentos.push(seg1);

	for (long long int i = 0; i < K-1; i++)
	{
		seg1 = segmentos.top();
		segmentos.pop();
		
		if( seg1.first > 1)
		{
			partir_Segmento(seg1,seg2);
			if( seg1.first > 0)
				segmentos.push(seg1);
			segmentos.push(seg2);
		}
	}
	
	seg1 = segmentos.top();
	segmentos.pop();
	
	//cout << " ganador ";print_seg(seg1);cout <<endl;
	
	int max = seg1.first/2;
	int min = max;
	if( seg1.first %2 == 0)
		min--;
	cout << max << " " << min;
	return;
}
//Crucemos los dedos
int main(){
	int T;
	long long int K,N; //Cambiar a long long int

	cin>>T;
	for (int i = 0; i < T; i++)
	{
		cin >> N >> K;
		cout<<"Case #"<<i+1<<": ";
		resolver(N,K);
		cout<<endl;
	}

	return 0;
}