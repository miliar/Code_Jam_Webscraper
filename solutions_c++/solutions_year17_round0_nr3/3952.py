#include<bits/stdc++.h>


using namespace std;
/*

Oh oh oh oh oh oh
You don't have to go oh oh oh oh oh
You don't have to go oh oh oh oh oh
You don't Have to go.

Ay ay ay ay ay ay
All those tears I cry ay ay ay ay ay
All those tears I cry ay ay ay ay ay
Baby please don't go.

[CHORUS:]
When I read the letter you wrote, it made me mad mad mad
When I read the words that it told me, it made me sad sad sad.
But I still love you so, I can't let you go
I love you- ooh baby I love you.

Oh oh oh oh oh oh
Every breath I take oh oh oh oh oh
Every move I make oh oh oh oh oh
Baby please don't go.

Ay ay ay ay ay ay
You hurt me to my soul ay ay ay ay ay
You hurt me to my soul ay ay ay ay ay
Darling please don't go.

[CHORUS 2:]
When I read the letter you sent me, it made me mad mad mad
When I read the news that it broke, it made me sad sad sad.
But I still love you so, and I can't let you go
I love you- ooh baby I love ya.
Oh oh oh oh oh oh
You don't have to go oh oh oh oh
You don't have to go oh oh oh oh
Aw Baby, babe Please Please Please Please
Ah uh ah uh ah ah baby
Ah Uh I still love you baby
Ooh Ooh, ooh ohh, ooh ooh Darling
Oh Oh-wo Aw baby I still love you so
Aw baby I still love you so oh-wo ooh

Oh oh oh oh oh oh yeah (fire)
Ah ah ah ah ah ah oh (fire)
Ah ah ah ah ah
Ooooh (fire) yeah
Oh Baby, Baby
*/
int main(){
priority_queue<long long > p;
    int testcases,chuiyahunmain=1;
    
    cin>>testcases;
    
    for(int i =0;i<testcases;i++){
        long long aagey,piche,temporaryvariable,k,n;
        cin>>k>>n;
        p.push(k);
		for(int ow =0 ;ow<1000;ow++){
			//main nhi tum bewakoof ho;
		}
        for(int j = 0;j<n;j++){
            temporaryvariable= p.top();
            
            
            temporaryvariable--;
            aagey=temporaryvariable/2;
			//ledzeppelin suno chuiyon
			piche=temporaryvariable/2;
            if(temporaryvariable%2==0){
                //piche+=1;
            }
            else
				piche++;
            p.pop();
            p.push(aagey);
			//cout<<"mera naam joker";
			p.push(piche);

            }
        cout<<"Case #";
		cout<<chuiyahunmain;
		cout<<": ";
		cout<<piche<<" "<<aagey<<endl;
        p = priority_queue <long long>();
        chuiyahunmain++;
    }
}
