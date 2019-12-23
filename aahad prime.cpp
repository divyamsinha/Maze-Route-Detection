#include<bits/stdc++.h>
using namespace std;
int main() {
    int t,n,val;
    cin >> t
	for(int o = 0 ; o < t ; o++)
    {
        val = 0 ;
        cin >> n ;
        for(int i = 1 ; i <= n ; i++)
        {
            val+=pow(-1,i-1)*pow(i,2);
        }
        if(val <0)
        cout << (val+100003%100003)<<endl;
        else cout << val%100003 << endl;
    }
}