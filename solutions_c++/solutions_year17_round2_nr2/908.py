#include<iostream>
#include<vector>
#include<map>
using namespace std;

int main(){
	int tt;
	cin >> tt;
	int n;
	
	for(int it = 0; it < tt; it ++){		
		cin >> n;
		
		int R, O, Y, G, B, V;
		cin >> R >> O >> Y >> G >> B >> V;
		//cout << R << Y << B << endl;
		R -= G;
		Y -= V;
		B -= O;
		
		
		cout << "Case #" << it + 1 << ": ";
		
		int notr = Y + B - R, noty = B + R - Y, notb = Y + R - B;
		if(R == 0 && G > 0 && O == 0 && Y == 0 && B == 0 && V == 0){
			for(int i = 0; i < G; i ++)cout << "RG";
			cout << endl;
		}
		else if(Y == 0 && V > 0 && O == 0 && R == 0 && B == 0 && G == 0){
			for(int i = 0; i < V; i ++)cout << "YV";
			cout << endl;
		}
		else if(B == 0 && O > 0 && R == 0 && Y == 0 && G == 0 && V == 0){
			for(int i = 0; i < O; i ++)cout << "BO";
			cout << endl;
		}
		else if(notr < 0 || noty < 0 || notb < 0 || R < 0 || (R == 0&&G>0) || Y < 0 || (Y == 0 && V>0) || B < 0 ||(B == 0 && O > 0))cout << "IMPOSSIBLE" << endl;
		else{
			int a[3];
			char b[3];
			string s = "";
			if(R <= Y && Y <= B){
				a[0] = R;
				a[1] = Y;
				a[2] = B;
				b[0] = 'R';
				b[1] = 'Y';
				b[2] = 'B';
			}
			else if(R <= B && B <= Y){
				a[0] = R;
				a[1] = B;
				a[2] = Y;
				b[0] = 'R';
				b[1] = 'B';
				b[2] = 'Y';
			}
			else if(Y <= R && R <= B){
				//cout << "!" << endl;
				a[0] = Y;
				a[1] = R;
				a[2] = B;
				b[0] = 'Y';
				b[1] = 'R';
				b[2] = 'B';
			}
			else if(Y <= B && B <= R){
				a[0] = Y;
				a[1] = B;
				a[2] = R;
				b[0] = 'Y';
				b[1] = 'B';
				b[2] = 'R';
			}
			else if(B <= R && R <= Y){
				a[0] = B;
				a[1] = R;
				a[2] = Y;
				b[0] = 'B';
				b[1] = 'R';
				b[2] = 'Y';
			}
			else{//} if(B <= Y <= R){
				a[0] = B;
				a[1] = Y;
				a[2] = R;
				b[0] = 'B';
				b[1] = 'Y';
				b[2] = 'R';
			}
			
			int k = a[2] - (a[1] - a[0]);
			int t = k / 2;
			//if(it == 2)cout << a[0] << a[1] << a[2];
			if(k % 2 == 0){
				
				for(int i = 0; i < t; i ++){
					s += b[2];
					s += b[0];
					s += b[2];
					s += b[1];
					//cout << b[2] << b[0] << b[2] << b[1];// "BRBY";
				}
				for(int i = 0; i < a[0] - t; i ++){
					s += b[0];
					s += b[1];
					//cout << b[0] << b[1];// "RY";
				}
				for(int i = 0; i < a[2] - 2 * t; i ++){
					s += b[2];
					s += b[1];
					//cout << b[2] << b[1];// "BY";
				}
			}
			else{
				for(int i = 0; i < t; i ++){
					s += b[2];
					s += b[0];
					s += b[2];
					s += b[1];
					//cout << b[2] << b[0] << b[2] << b[1];// "BRBY";
				}
				for(int i = 0; i < a[0] - t - 1; i ++){
					s += b[0];
					s += b[1];
					//cout << b[0] << b[1];// "RY";
				}
				s += b[0];
				s += b[2];
				s += b[1];
				//cout << b[0] << b[2] << b[1];// "RBY";
				for(int i = 0; i < a[2] - 2 * t - 1; i ++){
					s += b[2];
					s += b[1];
					//cout << b[2] << b[1];// "BY";
				}
			}
			//cout << s << endl;
			string rr = "R";
			string yy = "Y";
			string bb = "B";
			
			for(int i = 0; i < G; i ++)rr += "GR";
			for(int i = 0; i < V; i ++)yy += "VY";
			for(int i = 0; i < O; i ++)bb += "OB";
			int index;
			if(G>0){
			index = 0;
			while(s[index] != 'R')index ++;
			string ss = s.substr(0, index) + rr + s.substr(index + 1, s.length() - 1 - index);
			s = ss;}
			
			if(V>0){
			index = 0;
			while(s[index] != 'Y')index ++;
			string ss = s.substr(0, index) + yy + s.substr(index + 1, s.length() - 1 - index);
			s = ss;}
			
			if(O>0){
			index = 0;
			while(s[index] != 'B')index ++;
			string ss = s.substr(0, index) + bb + s.substr(index + 1, s.length() - 1 - index);
			s = ss;}
			cout << s << endl;
		}
	}
	return 0;
} 
