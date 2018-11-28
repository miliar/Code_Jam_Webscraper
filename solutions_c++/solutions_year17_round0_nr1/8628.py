#include <iostream>
#include <fstream>
#include <string>
#include <queue>
using namespace std;

int T,K;
struct Hash{
	string value;
}ELF[100008];
ofstream fout("fout.txt");
struct Node{
	string str;
	int step;
	Node(){
		str = "";
		step = 0;
	}
	Node(string s,int st){
		str = s;
		step = st;
	}
}S;

void Flip(string &str,int s,int e){
	for(int i = s ; i<e; i++)
		str[i] = !(str[i]-48)+48;
}

int ELFhash(string str){

	int i = 0;
    unsigned long h=0;
    unsigned long x=0;
	string s = "";

	
	
    while(str[i])
    {
        h=(h<<4)+str[i++];  //h左移4位，当前字符ASCII存入h的低四位
                if( (x=h & 0xF0000000L)!=0)
        { //如果最高位不为0，则说明字符多余7个，如果不处理，再加第九个字符时，第一个字符会被移出
          //因此要有如下处理
          h^=(x>>24);
          //清空28~31位
          h&=~x;
        }
    }
    return h % 100007;
}

int Ahash(string str){
	int key = ELFhash(str);
	int flag = 0;
	if( ELF[key].value == "" )
		ELF[key].value = str;
	else{
		while( ELF[key].value!=str ){
			key++;
			if( ELF[key].value == "" ){
				flag = 1;
				ELF[key].value = str;
				break;
			}
		}
		if( !flag )
			return 1;
		return 0;
	}
	return 0;
}

int BFS(Node s){
	int i,j;
	int flag = 1;
	Node F,N;
	string temp;
	queue<Node> Q;

	Q.push(s);
	F = Q.front();
	while(!Q.empty()){
		F = Q.front();
		if( F.str.find(48) == std::string::npos )
			return F.step;
		int hr = Ahash(F.str);

		if(hr){
			Q.pop();
			continue;
		}

		N.step = F.step+1;
		if(F.str == "0001111111")
			temp = "";
		for(i = F.str.length()-K; i>=0 ; i--){
			N.str = F.str;
			j = F.str.find(48,i);
			if( j == std::string::npos )
				continue;
			else if( j < i+K ){
				Flip(N.str,i,i+K);
				Q.push(N);
				if( N.str.find(48) == std::string::npos )
					return N.step;
			}
		}
		Q.pop();
	}
	return -1;
}

int main(){
	int t;
	int i,j,re;

	cin>>T;
	for( j = 1; j<=T ; j++){
		memset(ELF,0,sizeof(ELF));
		cin>>S.str>>K;
		for(i = 0 ; i < S.str.length() ; i++){
			if(S.str[i] == '-')
				S.str[i] = 48;
			else
				S.str[i] = 49;
		}
		re = BFS(S);
		fout<<"Case #"<<j<<": ";
		if( re == -1 )
			fout<<"IMPOSSIBLE"<<endl;
		else
			fout<<re<<endl;
	}
	system("pause");
	return 0;
}