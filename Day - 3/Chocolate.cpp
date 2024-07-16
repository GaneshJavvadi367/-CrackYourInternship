class Solution{
    public:
    long long findMinDiff(vector<long long> a, long long n, long long m){
        
        long long ans = 1e18;
        sort(a.begin(),a.end());
        int i = 0, j = i + (m - 1);
        
        while (j < n){
            ans = min(ans, a[j] - a[i]);
            j++;
            i++;
        }
         return ans;
    
    }   
};
