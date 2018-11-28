#include <iostream>  

using namespace std;  

#define swap(a,b){int tmp=a;a=b;b=tmp;}

long int is_tidy(long int N);


int main(int argc, char **argv)
{
	long int t,i;
	
	int T;
	long int* numbers;
	
	long int N;
	long int aux;
	
	cin >> T;
	
	numbers = new long int[T];
	
	for(t=0;t<T;t++)
	{
		cin >> numbers[t];
	}
	
	for(t=0;t<T;t++)
	{
		N=numbers[t];
		
		for(i=N;i>=0;i--)
		{
			aux=is_tidy(i);
			
			if(aux>0)
			{
				i=aux+1;
			}	
			else
			{
				if(aux==-1){cout << "Case #" << t+1 <<": "<< i << endl;break;}	
			}
		}
	}
	
	return 0;
}

long int lipow(long int base, int exp)
{
    long int result = 1;
    while (exp)
    {
        if (exp & 1){result *= base;}
        exp >>= 1;
        base *= base;
    }

    return result;
}

int numDigits (long int n) 
{
    if (n < 10) return 1;
    return 1 + numDigits (n / 10);
}

long int is_tidy(long int N)
{	
	int i,j;
	
	long int aux=N;

	int n_digits =numDigits(N);
	
	long int digits[n_digits];
	
	i=0;
	while(aux)
	{
		digits[i]=aux%10;
		aux /= 10;
		i++;
	}
	
	for (int i = 0; i < n_digits/ 2; ++i) 
	{
        swap(digits[i], digits[n_digits-i-1]);
    }
    
    
	for(i=0;i<n_digits-1;i++)
    {
		if(digits[i]>digits[i+1])
		{
			
			digits[i]--;
			j=i;
			while(digits[j]<0)
			{
				digits[j]=9;
				j--;
				digits[j-1]--;
			}

			for(j=i+1;j<n_digits;j++)
			{
				digits[j]=9;
			}
			
			aux=0;
			for(j=0;j<n_digits;j++)
			{
				aux+=digits[j]*lipow(10,n_digits-j-1);
			}
			
			return aux;
		}
	}
	
	return -1;
}
